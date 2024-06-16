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

    #for small 'e'
    # move_cmd.angular.z = 0
    # move_cmd.linear.x = 0.75
    # pub.publish(move_cmd)
    # rate.sleep()

    # move_cmd.angular.z = (PI/2)
    # move_cmd.linear.x = 0
    # pub.publish(move_cmd)
    # rate.sleep()

    # move_cmd.angular.z = (PI)
    # move_cmd.linear.x = (PI*0.5)
    # pub.publish(move_cmd)
    # rate.sleep()

    # move_cmd.angular.z = (0.8*PI)
    # move_cmd.linear.x = (PI)
    # pub.publish(move_cmd)
    # rate.sleep()

    move_cmd.angular.z = 0
    move_cmd.linear.x = 1
    pub.publish(move_cmd)
    rate.sleep()

    move_cmd.angular.z = 0
    move_cmd.linear.x = -1
    pub.publish(move_cmd)
    rate.sleep()

    move_cmd.angular.z = 0
    move_cmd.linear.x = 0
    pub.publish(move_cmd)
    rate.sleep()

    move_cmd.angular.z = 0
    move_cmd.linear.y = 1
    pub.publish(move_cmd)
    rate.sleep()

    move_cmd.angular.z = 0
    move_cmd.linear.y = 0
    pub.publish(move_cmd)
    rate.sleep()

    move_cmd.angular.z = 0
    move_cmd.linear.x = 1
    pub.publish(move_cmd)
    rate.sleep()

    move_cmd.angular.z = 0
    move_cmd.linear.x = -1
    pub.publish(move_cmd)
    rate.sleep()

    move_cmd.angular.z = 0
    move_cmd.linear.x = 0
    pub.publish(move_cmd)
    rate.sleep()

    move_cmd.angular.z = 0
    move_cmd.linear.y = 1
    pub.publish(move_cmd)
    rate.sleep()

    move_cmd.angular.z = 0
    move_cmd.linear.y = 0
    pub.publish(move_cmd)
    rate.sleep()

    move_cmd.angular.z = 0
    move_cmd.linear.x = 1
    pub.publish(move_cmd)
    rate.sleep()

    move_cmd.angular.z = 0
    move_cmd.linear.x = -1
    pub.publish(move_cmd)
    rate.sleep()

    move_cmd.angular.z = 0
    move_cmd.linear.x = 0
    pub.publish(move_cmd)
    rate.sleep()

    # h(move_cmd)
    # rate.sleep()

    
if __name__ == '__main__':
    try:
        move_spiral()
    except rospy.ROSInterruptException:
        pass
