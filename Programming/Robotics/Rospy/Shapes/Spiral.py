#!/usr/bin/env python3



import rospy
from geometry_msgs.msg  import Twist

# main function

    # initializing the node
    
rospy.init_node('rectangle', anonymous=True)
    
    # seting the topic on which all msgs have to publish
pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=20)
    
rate = rospy.Rate(1) # 1hz
    
    # storing twist msgs in veriable
vel_msg = Twist()
rate.sleep()
    
for i in range(1,20):
    vel_msg.linear.x = i/4 # m/s
    vel_msg.angular.z = (3.14/2) # r/s
    pub.publish(vel_msg)
    rate.sleep()
    i += 1