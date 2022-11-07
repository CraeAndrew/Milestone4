import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Joy

from std_msgs.msg import Int16

from drive_interfaces.msg import VehCmd

from geometry_msgs.msg import Twist

#from .ports import ports


import array
import math
import time

class Joy_Count(Node):

    def __init__(self):
        super().__init__('joy')
        self.subscription = self.create_subscription(
            Joy,'joy',self.listener_callback,10)
        self.subscription  # prevent unused variable warning

        self.timer = self.create_timer(3, self.timer_callback)
        
        self.publisher = self.create_publisher(Int16, 'led_color', 10)

        self.publisher2 = self.create_publisher(VehCmd, 'vehicle_command_angle', 10)


    

    def timer_callback(self):
        
        light = Int16()
        
        for i in range(1,3):
                        
            light.data = i

            self.get_logger().info('"%s"' % light.data)
            
            self.publisher.publish(light)

    def listener_callback(self, msg):

        control=VehCmd()
        
        control.throttle_effort = (msg.axes[1])*100
        control.steering_angle = (msg.axes[0])*45
    
        #self.get_logger().info('"%s"' % control)
        
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
