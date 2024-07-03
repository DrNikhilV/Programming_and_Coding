#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
import math

PI = 3.14

def move_inverted_U():
    rospy.init_node('move_inverted_U', anonymous=True)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(1)  # Adjust the rate as per your requirement

    move_cmd = Twist()

    move_cmd.angular.z = 0
    move_cmd.linear.x = 0
    pub.publish(move_cmd)
    rate.sleep()

    move_cmd.angular.z = -PI/2  # Inverted angular velocity for starting the inverted U shape
    move_cmd.linear.x = 0
    pub.publish(move_cmd)
    rate.sleep()

    move_cmd.linear.x = 3  # Adjust linear velocity for inverted U shape
    move_cmd.angular.z = 0  # Adjust linear velocity for inverted U shape
    pub.publish(move_cmd)
    rate.sleep()

    move_cmd.angular.z = PI/2  # Inverted angular velocity for turning in the inverted U shape
    move_cmd.linear.x = 2  # Adjust linear velocity for inverted U shape
    pub.publish(move_cmd)
    rate.sleep()

    move_cmd.linear.x = 1.5  # Adjust linear velocity for inverted U shape
    move_cmd.angular.z = 0  # Adjust linear velocity for inverted U shape
    pub.publish(move_cmd)
    rate.sleep()

    move_cmd.angular.z = PI/2  # Inverted angular velocity for turning in the inverted U shape
    move_cmd.linear.x = 2  # Adjust linear velocity for inverted U shape
    pub.publish(move_cmd)
    rate.sleep()

    move_cmd.linear.x = 3  # Adjust linear velocity for inverted U shape
    move_cmd.angular.z = 0  # Adjust linear velocity for inverted U shape
    pub.publish(move_cmd)
    rate.sleep()
if __name__ == '__main__':
    try:
        move_inverted_U()
    except rospy.ROSInterruptException:
        pass
