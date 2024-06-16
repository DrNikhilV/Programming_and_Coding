#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
import math

PI = 3.14

def move_spiral():
    rospy.init_node('move_spiral', anonymous=True)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(1)  # Adjust the rate as per your requirement

    move_cmd = Twist()

    for i in range(2):
        move_cmd.linear.x = 3  # Adjust linear velocity for spiral effect
        move_cmd.angular.z = PI  # Adjust linear velocity for spiral effect
        pub.publish(move_cmd)
        rate.sleep()
    for i in range(1):
        move_cmd.linear.x = 3  # Adjust linear velocity for spiral effect
        move_cmd.angular.z = -PI  # Adjust linear velocity for spiral effect
        pub.publish(move_cmd)
        rate.sleep()

if __name__ == '__main__':
    try:
        move_spiral()
    except rospy.ROSInterruptException:
        pass
