#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from math import pi

def draw_triangle():
    rospy.init_node('draw_triangle', anonymous=True)
    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
    rate = rospy.Rate(1) # 1hz
    
    vel_msg = Twist()
    
    # Move to start position
    vel_msg.linear.x = 2  # m/s
    vel_msg.angular.z = 0  # rad/s
    pub.publish(vel_msg)
    rospy.sleep(1)  # Adjust this sleep duration as necessary
    
    # Define the number of sides of the triangle
    num_sides = 3
    
    # Define the angle to turn for each side
    angle = 2 * pi / num_sides
    
    # Draw the triangle
    for _ in range(num_sides):
        # Turn
        vel_msg.linear.x = 0  # m/s
        vel_msg.angular.z = angle  # rad/s (turn angle)
        pub.publish(vel_msg)
        rospy.sleep(2)  # Adjust this sleep duration as necessary
        
        # Move forward
        vel_msg.linear.x = 2  # m/s
        vel_msg.angular.z = 0  # rad/s
        pub.publish(vel_msg)
        rospy.sleep(2)  # Adjust this sleep duration as necessary
    
    # Stop
    vel_msg.linear.x = 0
    vel_msg.angular.z = 0
    pub.publish(vel_msg)

    rospy.spin()

if __name__ == '__main__':
    try:
        draw_triangle()
    except rospy.ROSInterruptException:
        pass