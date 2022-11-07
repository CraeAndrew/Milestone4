import os
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    ld = LaunchDescription()
    motor_controller_node = Node(
        package="motor_driver",
        executable="motor_controller",
        parameters=[{"steering_offset": 0.0, "limiter": True}],
    )
    ld.add_action(motor_controller_node)
    return ld
