import carla
import random
import time


def change_weather_and_friction(world):
    weather_presets = [
        carla.WeatherParameters.ClearNoon,
        carla.WeatherParameters.CloudyNoon,
        carla.WeatherParameters.WetNoon,
        carla.WeatherParameters.MidRainyNoon,
        carla.WeatherParameters.HardRainNoon,
        carla.WeatherParameters.SoftRainNoon,
        carla.WeatherParameters.ClearSunset,
        carla.WeatherParameters.CloudySunset,
        carla.WeatherParameters.WetSunset,
        carla.WeatherParameters.MidRainSunset,
        carla.WeatherParameters.HardRainSunset,
        carla.WeatherParameters.SoftRainSunset
    ]

    friction_values = {
        carla.WeatherParameters.ClearNoon: 1.0,
        carla.WeatherParameters.CloudyNoon: 0.9,
        carla.WeatherParameters.WetNoon: 0.8,
        carla.WeatherParameters.MidRainyNoon: 0.7,
        carla.WeatherParameters.HardRainNoon: 0.6,
        carla.WeatherParameters.SoftRainNoon: 0.7,
        carla.WeatherParameters.ClearSunset: 1.0,
        carla.WeatherParameters.CloudySunset: 0.9,
        carla.WeatherParameters.WetSunset: 0.8,
        carla.WeatherParameters.MidRainSunset: 0.7,
        carla.WeatherParameters.HardRainSunset: 0.6,
        carla.WeatherParameters.SoftRainSunset: 0.7
    }

    while True:
        weather = random.choice(weather_presets)
        world.set_weather(weather)

        friction = friction_values[weather]
        set_road_friction(world, friction)

        time.sleep(3)  # 每10秒变换一次天气和摩擦力


def set_road_friction(world, friction_value):
    for actor in world.get_actors():
        if 'static.trigger' in actor.type_id:
            friction_bp = world.get_blueprint_library().find('static.trigger')
            friction_bp.set_attribute('friction', str(friction_value))
            transform = actor.get_transform()
            world.spawn_actor(friction_bp, transform)


def main():
    client = carla.Client('localhost', 2000)
    client.set_timeout(10.0)
    world = client.get_world()

    # 开始变换天气和摩擦力
    change_weather_and_friction(world)


if __name__ == '__main__':
    main()
