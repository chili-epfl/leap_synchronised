#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from std_msgs.msg import Header
from sensor_msgs.msg import Image
import message_filters
import threading
from threading import Thread
import time
starttime = time.time()

dataLeap = Image()

def readDataLeap(leap_data):
    global dataLeap
    dataLeap = leap_data

def save():
    global dataLeap
    # print("YES")
    if dataLeap.header.frame_id != "Empty":
        with open('../data/OnlyLeapData', 'a') as f:
            f.write(str(time.time()) + "|")
            f.write(str(dataLeap.header.stamp.secs + dataLeap.header.stamp.nsecs/1000000000.0) + "|" + str(dataLeap.header.frame_id) + '\n')
            dataLeap.header.stamp.secs = 0
            dataLeap.header.stamp.nsecs = 0
            dataLeap.header.frame_id = "Empty"
        
    threading.Timer(0.01, save).start()

if __name__ == "__main__":
    rospy.init_node("getDataLeap")
    rospy.Subscriber('dataLeap', Image, readDataLeap, queue_size=1)
    Thread(target=save, args=()).start()
    Thread(target=rospy.spin, args=()).start()
