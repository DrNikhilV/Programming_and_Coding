#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
import math

def draw_square():
    rospy.init_node('draw_star', anonymous=True)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(1)  # Adjust the rate as per your requirement

    move_cmd = Twist()

    # Adjusting linear and angular velocities for the square shape
      # Adjust the linear velocity for the side length of the square
    move_cmd.angular.z = 0.0  # No angular velocity initially

    # Executing loop 4 times for drawing a square
    for _ in range(6):
        move_cmd.linear.x = 3.0
        move_cmd.angular.z = 0.0
        pub.publish(move_cmd)
        rate.sleep()

        # Rotate the turtle 90 degrees for the next side
        move_cmd.linear.x = 0.0
        move_cmd.angular.z = 3.7593  # 144 degrees in radians
        pub.publish(move_cmd)
        rate.sleep()

    # Stop the turtle at the end
    move_cmd.angular.z = 0.0
    pub.publish(move_cmd)

if __name__ == '__main__':
    try:
        draw_square()
    except rospy.ROSInterruptException:
        pass

