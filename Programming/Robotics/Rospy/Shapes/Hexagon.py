#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from math import pi

def draw_rhombus():
    rospy.init_node('draw_rhombus', anonymous=True)
    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
    rate = rospy.Rate(1)  # 1hz

    vel_msg = Twist()

    # Move to start position
    vel_msg.linear.x = 2  # m/s
    vel_msg.angular.z = 0  # rad/s
    pub.publish(vel_msg)
    rospy.sleep(1)  # Adjust this sleep duration as necessary

    # Define the side length of the rhombus
    side_length = 2

    # Define the angle to turn for each corner of the rhombus
    angle = pi / 3  # 60 degrees in radians

    # Draw the rhombus
    for _ in range(8):
        # Move forward
        vel_msg.linear.x = side_length  # m/s
        vel_msg.angular.z = 0  # rad/s
        pub.publish(vel_msg)
        rospy.sleep(2)  # Adjust this sleep duration as necessary

        # Turn
        vel_msg.linear.x = 0  # m/s
        vel_msg.angular.z = angle  # rad/s (turn angle)
        pub.publish(vel_msg)
        rospy.sleep(2)  # Adjust this sleep duration as necessary

    # Stop
    vel_msg.linear.x = 0
    vel_msg.angular.z = 0
    pub.publish(vel_msg)

    rospy.spin()

if __name__ == '__main__':
    try:
        draw_rhombus()
    except rospy.ROSInterruptException:
        pass
