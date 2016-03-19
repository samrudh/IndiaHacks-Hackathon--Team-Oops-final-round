#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import ATT_IOT as IOT                  
from time import sleep                   #pause the app
import string

#set up the SmartLiving IoT platform
IOT.DeviceId = "8PQHkYNlXdXLfT9Nn9eD5DQ"			 #"8PQHkYNlXdXLfT9Nn9eD5DQ"
IOT.ClientId = "samrudh"
IOT.ClientKey = "wk5c3jb24j3"

results=[]
with open('input.txt') as inputfile:
    results = list(csv.reader(inputfile))
#number of devices N
str1 =  ""
str1 = ''.join(results[0])
a = str1.split('\t')
N=  a[1]

R=[]
A=[]
E=[]

#number of RPi R, Arduno A, intel Edision E
# R0 number of Rpi
# R1[0]= number of tem sensor  // number (float)
# R1[1]= Tmin
# R1[2]= Tmax
# R2[0] = number of level sensor  // int
# R2[1] = Lmin
# R2[2] = Lmax
# R3[0] = number of door sensor //boolean
# R= [R0, R1, R2, R3]

str1 =  ""
str1 = ''.join(results[2])
a = str1.split('\t')
R0=  a[2]
A0= a[4]
E0=a[6]

str1 =  ""
str1 = ''.join(results[3])
a = str1.split('\t')
R1=[a[2],a[3],a[4]]
R2=[a[6],a[7],a[8]]
R3=[a[10]]
R= [R0,R1,R2,R3]

str1 =  ""
str1 = ''.join(results[4])
a = str1.split('\t')
A1=[a[2],a[3],a[4]]
A2=[a[6],a[7],a[8]]
A3=[a[10]]
A= [A0,A1,A2,A3]

str1 =  ""
str1 = ''.join(results[5])
a = str1.split('\t')
E1=[a[2],a[3],a[4]]
E2=[a[6],a[7],a[8]]
E3=[a[10]]
E= [E0,E1,E2,E3]

inlist= [N,R,A,E]
#print inlist

#
IOT.connect()




sendpack()



     
