#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
import math

PI = math.pi

def move_spiral():
    rospy.init_node('move_spiral', anonymous=True)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(1)  # Adjust the rate as per your requirement

    move_cmd = Twist()

    move_cmd.angular.z = 0
    move_cmd.angular.y = 0
    move_cmd.angular.x = 0
    move_cmd.linear.x = 0
    move_cmd.linear.y = 0
    move_cmd.linear.z = 0
    pub.publish(move_cmd)
    rate.sleep()

    move_cmd.angular.z = PI/2
    move_cmd.linear.x = 0
    pub.publish(move_cmd)
    rate.sleep()

    move_cmd.linear.x = 3  # Adjust linear velocity for spiral effect
    move_cmd.angular.z = 0  # Adjust linear velocity for spiral effect
    pub.publish(move_cmd)
    rate.sleep()

    move_cmd.linear.x = 0  # Adjust linear velocity for spiral effect
    move_cmd.angular.z = PI/2  # Adjust linear velocity for spiral effect
    pub.publish(move_cmd)
    rate.sleep()

    move_cmd.linear.x = 2  # Adjust linear velocity for spiral effect
    move_cmd.angular.z = 0  # Adjust linear velocity for spiral effect
    pub.publish(move_cmd)
    rate.sleep()

    move_cmd.linear.x = 0  # Adjust linear velocity for spiral effect
    move_cmd.angular.z = PI  # Adjust linear velocity for spiral effect
    pub.publish(move_cmd)
    rate.sleep()


    move_cmd.linear.x = 4  # Adjust linear velocity for spiral effect
    move_cmd.angular.z = 0  # Adjust linear velocity for spiral effect
    pub.publish(move_cmd)
    rate.sleep()

if __name__ == '__main__':
    try:
        move_spiral()
    except rospy.ROSInterruptException:
        pass
