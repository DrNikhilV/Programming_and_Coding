#!/usr/bin/env python3



import rospy
from geometry_msgs.msg  import Twist

# main function
def rectangle():

    # initializing the node
    rospy.init_node('rectangle', anonymous=True)

    # seting the topic on which all msgs have to publish
    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=20)

    rate = rospy.Rate(1) # 1hz

    # storing twist msgs in veriable
    vel_msg = Twist()
    rate.sleep()

    for i in range(2):
        #Forward
        vel_msg.linear.x = 0 # m/s
        vel_msg.angular.z = 3*(3.14/2) # r/s
        pub.publish(vel_msg)
        rate.sleep()

        #Stop
        vel_msg.linear.x = 2 # m/s
        vel_msg.angular.z = 0 # r/s
        pub.publish(vel_msg)
        rate.sleep()

        #Turn
        vel_msg.linear.x = 0 # m/s
        vel_msg.angular.z= 3*(3.14/2) #r/s
        pub.publish(vel_msg)
        rate.sleep()

        vel_msg.linear.x = 2 # m/s
        vel_msg.angular.z = 0 # r/s
        pub.publish(vel_msg)
        rate.sleep()
if __name__ == '__main__':
    rectangle()
