#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from math import pi

def draw_star():
    rospy.init_node('draw_star', anonymous=True)
    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
    rate = rospy.Rate(1)  # 1hz

    vel_msg = Twist()

    # Move to start position
    vel_msg.linear.x = 2  # m/s
    vel_msg.angular.z = 0  # rad/s
    pub.publish(vel_msg)
    rospy.sleep(1)  # Adjust this sleep duration as necessary

    # Define the number of points of the star
    num_points = 5

    # Define the angle to turn for each point
    angle = 2 * pi / num_points

    # Draw the star
    for _ in range(num_points):
        # Move forward
        vel_msg.linear.x = 2  # m/s
        vel_msg.angular.z = 0  # rad/s
        pub.publish(vel_msg)
        rospy.sleep(2)  # Adjust this sleep duration as necessary

        # Turn
        vel_msg.linear.x = 0  # m/s
        vel_msg.angular.z = 2 * angle  # rad/s (turn angle)
        pub.publish(vel_msg)
        rospy.sleep(2)  # Adjust this sleep duration as necessary

    # Stop
    vel_msg.linear.x = 0
    vel_msg.angular.z = 0
    pub.publish(vel_msg)

    rospy.spin()

if __name__ == '__main__':
    try:
        draw_star()
    except rospy.ROSInterruptException:
        pass