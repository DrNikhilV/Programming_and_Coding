#!/usr/bin/env python3

import rospy
from geometry_msgs.msg  import Twist
from  math import pi
# main function


    # initializing the node
rospy.init_node('rectangle', anonymous=True)

    # seting the topic on which all msgs have to publish
pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=20)

rate = rospy.Rate(1) # 1hz

    # storing twist msgs in veriable
vel_msg = Twist()

vel_msg.linear.x = 0 # m/s
vel_msg.angular.z = 0 # r/s
pub.publish(vel_msg)
rate.sleep()

vel_msg.linear.x = 0 # m/s
vel_msg.angular.z = pi/2 # r/s
pub.publish(vel_msg)
rate.sleep()

vel_msg.linear.x = 2 # m/s
vel_msg.angular.z = 0 # r/s
pub.publish(vel_msg)
rate.sleep()

vel_msg.linear.x = 0 # m/s
vel_msg.angular.z = pi # r/s
pub.publish(vel_msg)
rate.sleep()

vel_msg.linear.x = 1 # m/s
vel_msg.angular.z = 0 # r/s
pub.publish(vel_msg)
rate.sleep()

vel_msg.linear.x = 0 # m/s
vel_msg.angular.z = (3*pi)/4 # r/s
pub.publish(vel_msg)
rate.sleep()

vel_msg.linear.x = 1 # m/s
vel_msg.angular.z = 0 # r/s
pub.publish(vel_msg)
rate.sleep()

vel_msg.linear.x = 0 # m/s
vel_msg.angular.z = pi # r/s
pub.publish(vel_msg)
rate.sleep()

vel_msg.linear.x = 1 # m/s
vel_msg.angular.z = 0 # r/s
pub.publish(vel_msg)
rate.sleep()

vel_msg.linear.x = 0 # m/s
vel_msg.angular.z = pi/2 # r/s
pub.publish(vel_msg)
rate.sleep()

vel_msg.linear.x = 1 # m/s
vel_msg.angular.z = 0 # r/s
pub.publish(vel_msg)
rate.sleep()