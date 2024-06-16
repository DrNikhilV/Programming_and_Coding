#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
import math

def move_spiral():
    rospy.init_node('move_spiral', anonymous=True)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(1)  # Adjust the rate as per your requirement

    move_cmd = Twist()
    
    for i in range(100):
        move_cmd.linear.x = i * 0.05  # Adjust linear velocity for spiral effect
        move_cmd.linear.y = i * 0.05  # Adjust linear velocity for spiral effect
        move_cmd.angular.z = 0.5  # Adjust angular velocity for smooth rotation
        pub.publish(move_cmd)
        rate.sleep()

if __name__ == '__main__':
    try:
        move_spiral()
    except rospy.ROSInterruptException:
        pass
