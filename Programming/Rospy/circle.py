#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

def draw_circle():
    rospy.init_node('circle', anonymous=True)
    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
    rate = rospy.Rate(1) # 1hz
    vel_msg = Twist()
    # Move in a circle
    for _ in range(10): # Adjust this loop count to control the size of the circle
        vel_msg.linear.x = 1  # m/s
        vel_msg.angular.z = 1  # rad/s (adjust for desired angular velocity)
        pub.publish(vel_msg)
        rate.sleep()

    # Stop
    vel_msg.linear.x = 0
    vel_msg.angular.z = 0
    pub.publish(vel_msg)

    rospy.spin()

if __name__ == '__main__':
	draw_circle()