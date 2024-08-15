import carla
import random
import time
import numpy as np
import cv2
import os

def change_weather_and_friction(world):
    weather_presets = [
        carla.WeatherParameters.ClearNoon,
        carla.WeatherParameters.HardRainNoon,
        carla.WeatherParameters.ClearSunset,
        carla.WeatherParameters.HardRainSunset,
        carla.WeatherParameters.WetNoon,
        carla.WeatherParameters.WetSunset,
        carla.WeatherParameters.MidRainSunset,
    ]

    friction_values = {
        carla.WeatherParameters.ClearNoon: 1.0,
        carla.WeatherParameters.HardRainNoon: 0.5,
        carla.WeatherParameters.ClearSunset: 1.0,
        carla.WeatherParameters.HardRainSunset: 0.5,
        carla.WeatherParameters.WetNoon: 0.7,
        carla.WeatherParameters.WetSunset: 0.7,
        carla.WeatherParameters.MidRainSunset: 0.5,
    }

    while True:
        weather = random.choice(weather_presets)
        world.set_weather(weather)

        friction = friction_values[weather]
        set_road_friction(world, friction)

        time.sleep(3)

def set_road_friction(world, friction_value):
    for actor in world.get_actors():
        if 'static.trigger' in actor.type_id:
            friction_bp = world.get_blueprint_library().find('static.trigger')
            friction_bp.set_attribute('friction', str(friction_value))
            transform = actor.get_transform()
            world.spawn_actor(friction_bp, transform)

def spawn_hgv(world, blueprint_library):
    spawn_points = world.get_map().get_spawn_points()

    # 手动选择一个接近地图下方的spawn point
    chosen_spawn_point = None
    for sp in spawn_points:
        if sp.location.y < -100 and sp.location.x < -100:  # 这里以 y 轴小于 -50 为例，表示地图靠下的区域
            chosen_spawn_point = sp
            break

    # 如果没有找到合适的点，默认使用第一个生成点
    if not chosen_spawn_point:
        chosen_spawn_point = random.choice(spawn_points)

    hgv_bp = blueprint_library.filter('vehicle.carlamotors.carlacola')[0]
    vehicle = world.spawn_actor(hgv_bp, chosen_spawn_point)
    return vehicle


def attach_camera_to_vehicle(world, vehicle):
    camera_bp = world.get_blueprint_library().find('sensor.camera.rgb')

    # 设定第三人称视角的位置：在车辆后方6米，抬高2.5米
    camera_transform = carla.Transform(carla.Location(x=-15, z=15), carla.Rotation(pitch=-30))

    camera = world.spawn_actor(camera_bp, camera_transform, attach_to=vehicle)
    camera_bp.set_attribute('image_size_x', '800')
    camera_bp.set_attribute('image_size_y', '600')
    return camera

def drive_hgv(vehicle):
    vehicle.set_autopilot(True)

def process_camera_image(image, video_writer):
    # 将CARLA图像转换为OpenCV图像
    array = np.frombuffer(image.raw_data, dtype=np.dtype("uint8"))
    array = np.reshape(array, (image.height, image.width, 4))  # 原始数据为BGRA格式
    array = array[:, :, :3]  # 保留BGR三个通道，去掉Alpha通道

    # 直接写入视频文件（BGR格式）
    video_writer.write(array)

def main():
    client = carla.Client('localhost', 2000)
    client.set_timeout(10.0)
    world = client.load_world('Town07')
    blueprint_library = world.get_blueprint_library()

    hgv = spawn_hgv(world, blueprint_library)
    camera = attach_camera_to_vehicle(world, hgv)

    save_path = os.path.join('..', 'Video', 'output.mp4')
    video_writer = cv2.VideoWriter(save_path, cv2.VideoWriter_fourcc(*'mp4v'), 30, (800, 600))

    camera.listen(lambda image: process_camera_image(image, video_writer))
    drive_hgv(hgv)

    try:
        change_weather_and_friction(world)
        time.sleep(60)
    except KeyboardInterrupt:
        print('KeyboardInterrupt detected. Exiting...')
    finally:
        # 停止传感器并释放资源
        camera.stop()
        video_writer.release()
        print(f"Video saved as {save_path}")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Exiting...')
        cv2.destroyAllWindows()
