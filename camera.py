import math


def relative_angle(drone, target):
    dx = target.x - drone.x
    dy = target.y - drone.y

    target_angle = math.atan2(dy, dx)
    angle_difference = target_angle - drone.theta

    angle_difference = math.atan2(
        math.sin(angle_difference),
        math.cos(angle_difference)
    )

    return angle_difference


def is_in_fov(drone, target, fov_deg=60, max_range=30):
    angle = relative_angle(drone, target)
    half_fov = math.radians(fov_deg / 2)

    dx = target.x - drone.x
    dy = target.y - drone.y

    distance = math.hypot(dx, dy)

    return abs(angle) <= half_fov and distance <= max_range
