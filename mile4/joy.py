import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Joy

from std_msgs.msg import Int16

from drive_interfaces.msg import VehCmd

from nav_msgs.msg import Odometry

from geometry_msgs.msg import Twist

import array
import math
import time

class Joy_Count(Node):

    def __init__(self):
        super().__init__('joy')
        self.subscription = self.create_subscription(
            Joy,'joy',self.listener_callback,10)

        self.subscription2 = self.create_subscription(
            Odometry,'odometry',self.listener_callback2,10)

        self.subscription  # prevent unused variable warning
        self.subscription2

        self.time_old = time.monotonic()
        self.sum = 0
        self.e_old = 0
        self.timer = self.create_timer(3, self.timer_callback)
        
        self.publisher = self.create_publisher(Int16, 'led_color', 10)
        self.publisher2 = self.create_publisher(VehCmd, 'vehicle_command_angle', 10)
        
    def timer_callback(self):
        
        light = Int16()
        
        for i in range(1,3):
                        
            light.data = i
            
            self.publisher.publish(light)

    def listener_callback(self, msg):

        
        self.r = (msg.axes[1])*100
        self.r2 = (msg.axes[0])*45


    def listener_callback2(self, msg):
        control=VehCmd()

        y = 100.0*msg.twist.twist.linear.x/7.3513268

        e = self.r-y
        
        kp = 0.5
        ki = 0.2
        kd = 0.2

        self.time_now = time.monotonic()
        delta_t = self.time_now - self.time_old
        self.time_old = self.time_now

        self.sum = self.sum + e*delta_t

        u = (kp*e) + (ki*self.sum) + (kd*(e-self.e_old)/delta_t)
        
        if u > 100.0:
            u = 100.0
            
        if u < -100.0:
            u = -100.0
        
        self.e_old = e

        control.throttle_effort = u
        control.steering_angle = self.r2
        
        self.publisher2.publish(control)


def main(args=None):
    rclpy.init(args=args)

    joy = Joy_Count()

    rclpy.spin(joy)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    joy.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
