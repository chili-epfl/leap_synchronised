#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from std_msgs.msg import Header
from sensor_msgs.msg import Image
import message_filters
import threading
import time
starttime=time.time()

def callback(leap_data, wacom_data):
    print("Leap: " + str(leap_data.header.stamp) + str(leap_data.header.frame_id) + '\n')
    print("Wacom: " + str(wacom_data.header.stamp) + str(wacom_data.header.frame_id) + '\n')

rospy.init_node("getDataLeapWacom")

leap_sub = message_filters.Subscriber('dataLeap', Image)
wacom_sub = message_filters.Subscriber('dataWacom_header', Image)
ts = message_filters.ApproximateTimeSynchronizer([leap_sub, wacom_sub], 10, 0.001)
ts.registerCallback(callback)
rospy.spin()