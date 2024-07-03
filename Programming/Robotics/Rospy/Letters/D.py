#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
import math

PI = 3.14

def move_D():
    rospy.init_node('move_D', anonymous=True)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(1)  # Adjust the rate as per your requirement

    move_cmd = Twist()

    move_cmd.angular.z = 0
    move_cmd.linear.x = 0
    pub.publish(move_cmd)
    rate.sleep()

    move_cmd.angular.z = -PI/2  # Angular velocity for starting the shape of letter "D"
    move_cmd.linear.x = 0
    pub.publish(move_cmd)
    rate.sleep()

    move_cmd.linear.x = 3  # Adjust linear velocity for the straight part of letter "D"
    move_cmd.angular.z = 0  # Adjust angular velocity for the straight part of letter "D"
    pub.publish(move_cmd)
    rate.sleep()

    move_cmd.angular.z = PI/2  # Angular velocity for turning inwards to form the curve of letter "D"
    move_cmd.linear.x = 0  # Adjust linear velocity for the curve of letter "D"
    pub.publish(move_cmd)
    rate.sleep()

    move_cmd.angular.z = 0  # Stop turning
    move_cmd.linear.x = 3  # Continue straight to complete the shape of letter "D"
    pub.publish(move_cmd)
    rate.sleep()

    move_cmd.angular.z = PI/2  # Inverted angular velocity for turning in the inverted U shape
    move_cmd.linear.x = 2  # Adjust linear velocity for inverted U shape
    pub.publish(move_cmd)
    rate.sleep()

    move_cmd.linear.x = 0.9  # Adjust linear velocity for inverted U shape
    move_cmd.angular.z = 0  # Adjust linear velocity for inverted U shape
    pub.publish(move_cmd)
    rate.sleep()

    move_cmd.angular.z = PI/2  # Inverted angular velocity for turning in the inverted U shape
    move_cmd.linear.x = 2  # Adjust linear velocity for inverted U shape
    pub.publish(move_cmd)
    rate.sleep()

    move_cmd.linear.x = 2.8  # Adjust linear velocity for inverted U shape
    move_cmd.angular.z = 0  # Adjust linear velocity for inverted U shape
    pub.publish(move_cmd)
    rate.sleep()


if __name__ == '__main__':
    try:
        move_D()
    except rospy.ROSInterruptException:
        pass
