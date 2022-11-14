import os
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    ld = LaunchDescription()

    joy_node = Node(
        package="joy",
        executable="joy_node",
        #parameters=[{"steering_offset": 0.0}],
    )
    ld.add_action(joy_node)

    joy = Node(
        package="mile4",
        executable="joy",
        #parameters=[{"Up": 0.0},
        #            {"Ui": 0.0},
        #            {"Ud": 0.0}
        #]
    )
    ld.add_action(joy)

    motor_controller_node = Node(
        package="motor_driver",
        executable="motor_controller",
        parameters=[{"steering_offset": 0.0, "limiter": False}],
    )
    ld.add_action(motor_controller_node)

    return ld
