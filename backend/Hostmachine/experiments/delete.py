#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import ATT_IOT as IOT                  
from time import sleep                   #pause the app
import string
import random
from random import randint
import thread
from sys import exit
import os



IOT.ClientId = "teamoopsindiahacks"
IOT.ClientKey ="5zgkgpfpxee"

#old setting working
#IOT.ClientId = "indiahack_oops"
#IOT.ClientKey ="1tbxrq5itbs"
IOT.connect()


# delete the output file devicess.txt

results=[]
with open('devicess.txt') as inputfile:
    results = list(csv.reader(inputfile))
    str1 =  ""
    print "inside file read"
    for line in results:
        print "inside lines... "
        str1 = ''.join(line)
        a = str1.split('\t')
        name= a[0]
        idd = 0
        IOT.DeviceId = str(a[1])
        print "This id deviceid:" + '\n'
        print IOT.DeviceId
       
        IOT.deleteDevice()
