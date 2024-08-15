import glob
import os
import sys
import carla
import argparse
from queue import Queue, Empty
import numpy as np
from matplotlib import cm
import cv2

VIRIDIS = np.array(cm.get_cmap('viridis').colors)
VID_RANGE = np.linspace(0.0, 1.0, VIRIDIS.shape[0])

def sensor_callback(data, queue):
    queue.put(data)

def tutorial(args):
    client = carla.Client(args.host, args.port)
    client.set_timeout(10.0)
    world = client.get_world()
    bp_lib = world.get_blueprint_library()

    traffic_manager = client.get_trafficmanager(8000)
    traffic_manager.set_synchronous_mode(True)

    original_settings = world.get_settings()
    settings = world.get_settings()
    settings.synchronous_mode = True
    settings.fixed_delta_seconds = 0.05
    world.apply_settings(settings)

    vehicle = None
    lidar = None
    video_writer = None
    previous_frame_data = None

    try:
        if not os.path.isdir('_out'):
            os.mkdir('_out')

        vehicle_bp = bp_lib.filter("vehicle.lincoln.mkz_2017")[0]
        lidar_bp = bp_lib.filter("sensor.lidar.ray_cast")[0]

        lidar_bp.set_attribute('range', str(args.range))
        lidar_bp.set_attribute('points_per_second', str(args.points_per_second))
        lidar_bp.set_attribute('channels', str(args.channels))
        lidar_bp.set_attribute('upper_fov', str(args.upper_fov))
        lidar_bp.set_attribute('lower_fov', str(args.lower_fov))
        if args.no_noise:
            lidar_bp.set_attribute('dropoff_general_rate', '0.0')
            lidar_bp.set_attribute('dropoff_intensity_limit', '1.0')
            lidar_bp.set_attribute('dropoff_zero_intensity', '0.0')

        spawn_points = world.get_map().get_spawn_points()
        selected_spawn_point = spawn_points[0]

        vehicle = world.spawn_actor(
            blueprint=vehicle_bp,
            transform=selected_spawn_point)
        vehicle.set_autopilot(True)

        traffic_manager.vehicle_percentage_speed_difference(vehicle, 50)  # Reduce speed by 50%

        lidar_transform = carla.Transform(
            carla.Location(x=0.0, z=2.5),
            carla.Rotation(pitch=-10))

        lidar = world.spawn_actor(
            blueprint=lidar_bp,
            transform=lidar_transform,
            attach_to=vehicle)

        save_path = '_out/lidar_output.mp4'
        video_writer = cv2.VideoWriter(save_path, cv2.VideoWriter_fourcc(*'mp4v'), 30, (args.width, args.height))

        lidar_visualization = np.zeros((args.height, args.width, 3), dtype=np.uint8)
        lidar_queue = Queue()
        lidar.listen(lambda data: sensor_callback(data, lidar_queue))

        for frame in range(args.frames):
            world.tick()
            world_frame = world.get_snapshot().frame

            try:
                lidar_data = lidar_queue.get(True, 1.0)
            except Empty:
                print("[Warning] Some sensor data has been missed")
                continue

            p_cloud_size = len(lidar_data)
            p_cloud = np.frombuffer(lidar_data.raw_data, dtype=np.dtype('f4'))
            p_cloud = np.reshape(p_cloud, (p_cloud_size, 4))

            if p_cloud_size == 0:
                print(f"Frame {frame+1}/{args.frames}: No LiDAR points captured.")
                continue

            lidar_visualization[:] = 0

            intensity = np.array(p_cloud[:, 3])
            max_intensity = np.max(intensity)
            intensity /= max_intensity  # Normalize intensity across the entire point cloud

            u_coord = (p_cloud[:, 0] * 5 + args.width // 2).astype(np.int32)
            v_coord = (p_cloud[:, 1] * 5 + args.height // 2).astype(np.int32)

            valid_mask = (u_coord >= 0) & (u_coord < args.width) & (v_coord >= 0) & (v_coord < args.height)
            u_coord = u_coord[valid_mask]
            v_coord = v_coord[valid_mask]
            intensity = intensity[valid_mask]

            color_map = np.array([
                np.interp(intensity, VID_RANGE, VIRIDIS[:, 0]) * 255.0,
                np.interp(intensity, VID_RANGE, VIRIDIS[:, 1]) * 255.0,
                np.interp(intensity, VID_RANGE, VIRIDIS[:, 2]) * 255.0]).astype(np.int32).T

            for i in range(len(u_coord)):
                cv2.circle(lidar_visualization, (u_coord[i], v_coord[i]), args.dot_extent, color_map[i].tolist(), -1)

            # Blend current frame with previous frame data to reduce flickering
            if previous_frame_data is not None:
                lidar_visualization = cv2.addWeighted(lidar_visualization, 0.5, previous_frame_data, 0.5, 0)

            previous_frame_data = lidar_visualization.copy()

            video_writer.write(lidar_visualization)

            print(f"Frame {frame+1}/{args.frames} processed.")

    finally:
        world.apply_settings(original_settings)
        if lidar:
            lidar.stop()
            lidar.destroy()
        if vehicle:
            vehicle.destroy()
        if video_writer:
            video_writer.release()
            print(f"LiDAR video saved as {save_path}")

def main():
    argparser = argparse.ArgumentParser(
        description='CARLA LiDAR recording example')
    argparser.add_argument(
        '--host',
        metavar='H',
        default='127.0.0.1',
        help='IP of the host server (default: 127.0.0.1)')
    argparser.add_argument(
        '-p', '--port',
        metavar='P',
        default=2000,
        type=int,
        help='TCP port to listen to (default: 2000)')
    argparser.add_argument(
        '--res',
        metavar='WIDTHxHEIGHT',
        default='800x600',
        help='window resolution (default: 800x600)')
    argparser.add_argument(
        '-f', '--frames',
        metavar='N',
        default=500,
        type=int,
        help='number of frames to record (default: 500)')
    argparser.add_argument(
        '-d', '--dot-extent',
        metavar='SIZE',
        default=1,
        type=int,
        help='visualization dot extent in pixels (Recomended [1-4]) (default: 1)')
    argparser.add_argument(
        '--no-noise',
        action='store_true',
        help='remove the drop off and noise from the normal (non-semantic) lidar')
    argparser.add_argument(
        '--upper-fov',
        metavar='F',
        default=30.0,
        type=float,
        help='lidar\'s upper field of view in degrees (default: 30.0)')
    argparser.add_argument(
        '--lower-fov',
        metavar='F',
        default=-30.0,
        type=float,
        help='lidar\'s lower field of view in degrees (default: -30.0)')
    argparser.add_argument(
        '-c', '--channels',
        metavar='C',
        default=64.0,
        type=float,
        help='lidar\'s channel count (default: 64)')
    argparser.add_argument(
        '-r', '--range',
        metavar='R',
        default=100.0,
        type=float,
        help='lidar\'s maximum range in meters (default: 100.0)')
    argparser.add_argument(
        '--points-per-second',
        metavar='N',
        default='100000',
        type=int,
        help='lidar points per second (default: 100000)')
    args = argparser.parse_args()
    args.width, args.height = [int(x) for x in args.res.split('x')]

    try:
        tutorial(args)

    except KeyboardInterrupt:
        print('\nCancelled by user. Bye!')

if __name__ == '__main__':
    main()

