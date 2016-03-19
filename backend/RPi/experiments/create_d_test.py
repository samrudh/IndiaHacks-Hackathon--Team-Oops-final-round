#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import ATT_IOT as IOT                  
from time import sleep                   #pause the app

#set up the SmartLiving IoT platform
IOT.DeviceId = 0			 #"8PQHkYNlXdXLfT9Nn9eD5DQ"
IOT.ClientId = "samrudh"
IOT.ClientKey = "wk5c3jb24j3"


'''creates a new device. The Id of the device will be stored in Devic$
    :param name: the name of the device
    :param description: an optional description
    :param activityEnabled: When True, historical data will be stored in $
    
addAsset(id, name, description, isActuator, assetType, style = "Undefined"):
IOT.addAsset(lightSensor, "lightSensor", "Light Sensor", False, "integer")
'''


results=[]
with open('input.txt') as inputfile:
    results = list(csv.reader(inputfile))
#number of devices N
str1 =  ""
str1 = ''.join(results[0])
a = str1.split('\t')
N=  a[1]

#number of RPi R, Arduno A, intel Edision E 
str1 = ""
str1 = ''.join(results[2])
a = str1.split('\t')
R= a[2]
A= a[4]
E= a[6]
inlist=[N,R,A,E]

def setup(mylist):
    R=int(mylist[1])
    A=int(mylist[2])
    E=int(mylist[3])
    IOT.connect()
    
    for x in range(0, R):
        dtype = "RaspberryPi" + str(x)
        print("complete device name: "+dtype)
        devlist=IOT.createDevice(dtype, "lightSensor", True)
        with open('devicess.txt', 'a') as file_:
            file_.write(devlist[1] + " "+devlist [0] + '\n')

    for x in range(0, A):
        dtype = "Arduino" +str(x)
        devlist=IOT.createDevice(dtype, "lightSensor", True)
        with open('devicess.txt', 'a') as file_:
            file_.write(devlist[1] + " "+devlist [0] + '\n')

    for x in range(0, E):
        dtype = "IntelDevice"+str(x)
        devlist=IOT.createDevice(dtype, "lightSensor", True)
        with open('devicess.txt', 'a') as file_:
            file_.write(devlist[1] + " "+devlist [0] + '\n')
        IOT.deleteDevice()
        
setup(inlist)

