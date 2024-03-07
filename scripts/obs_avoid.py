#!/usr/bin/env python3
# /**
#  * @file obs_avoid.py
#  * @author Sameer Arjun S (ssarjun@umd.edu)
#  * @brief This program moves the turtle in Gazebo by avoiding
#  * obstacles using LIDAR
#  * @copyright Copyright (c) 2023
#  * This code is licensed under the Apache 2.0 License. Please see the
#  * accompanying LICENSE file for the full text of the license
#  */

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

class TurtlebotNavigation(Node):
    def __init__(self):
        super().__init__('turtlebot_navigation')
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        self.laser_scan_subscriber_ = self.create_subscription(LaserScan, '/scan', self.laser_scan_callback, 5)

    def laser_scan_callback(self, msg):
        if msg.header.stamp.sec == 0:
            return
        scan_data = msg.ranges
        field_range = 60
        initial_angle = 330
        obstacle_detected = False

        for i in range(initial_angle, initial_angle + field_range):
            if scan_data[i % 360] < 0.75:
                obstacle_detected = True
                break
        if obstacle_detected:
            self.rotate_inplace(0.3)
        else:
            self.move_forward(0.5)

    def move_forward(self, translate_velocity):
        velocity_msg = Twist()
        velocity_msg.linear.x = translate_velocity
        velocity_msg.angular.z = 0.0
        self.publisher_.publish(velocity_msg)

    def rotate_inplace(self, rotation_velocity):
        velocity_msg = Twist()
        velocity_msg.linear.x = 0.0
        velocity_msg.angular.z = rotation_velocity
        self.publisher_.publish(velocity_msg)

def main(args=None):
    rclpy.init(args=args)
    turtlebot_navigation = TurtlebotNavigation()
    rclpy.spin(turtlebot_navigation)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
