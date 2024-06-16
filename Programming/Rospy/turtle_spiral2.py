#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
import math

def move_spiral():
    rospy.init_node('move_spiral', anonymous=True)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(1)  # Adjust the rate as per your requirement

    move_cmd = Twist()
    
    for i in range(20):
        move_cmd.linear.x = i/4    # Increase linear velocity gradually for spiral effect
        move_cmd.angular.z = 3.14/2 # Constant angular velocity for smooth rotation
        pub.publish(move_cmd)
        rate.sleep()

if __name__ == '__main__':
    try:
        move_spiral()
    except rospy.ROSInterruptException:
        pass

