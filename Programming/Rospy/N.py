#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
import math

PI = 3.14

def move_n():
    rospy.init_node('move_n', anonymous=True)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(1)  # Adjust the rate as per your requirement

    move_cmd = Twist()

    move_cmd.angular.z = 0
    move_cmd.linear.x = 0
    pub.publish(move_cmd)
    rate.sleep()

    # Move forward
    move_cmd.linear.x = 2
    move_cmd.angular.z = 0
    pub.publish(move_cmd)
    rate.sleep()

    # Turn right
    move_cmd.angular.z = -PI/2
    move_cmd.linear.x = 0
    pub.publish(move_cmd)
    rate.sleep()

    # Move forward
    move_cmd.linear.x = 2
    move_cmd.angular.z = 0
    pub.publish(move_cmd)
    rate.sleep()

    # Diagonal line (right to left)
    move_cmd.angular.z = PI/3
    move_cmd.linear.x = 2
    pub.publish(move_cmd)
    rate.sleep()

    # Diagonal line (left to right)
    move_cmd.angular.z = -PI/3
    move_cmd.linear.x = 1
    pub.publish(move_cmd)
    rate.sleep()

    # Turn right
    move_cmd.angular.z = -PI/2
    move_cmd.linear.x = 0
    pub.publish(move_cmd)
    rate.sleep()

    # Move forward
    move_cmd.linear.x = 2
    move_cmd.angular.z = 0
    pub.publish(move_cmd)
    rate.sleep()

if __name__ == '__main__':
    try:
        move_n()
    except rospy.ROSInterruptException:
        pass
