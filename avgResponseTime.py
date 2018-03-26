# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 15:55:47 2018

@author: khann
"""

import pandas as pd
import math


def outlier(arg): #this function determines the bounds for an outlier

    num = len(arg)
    arg = sorted(arg) #sorting the list
    mid = int(num/2)    #median value
    Q1 = int(mid/2)+4
    Q3 = mid + int(mid/2)
    


    IQR = arg[Q3] - arg[Q1]
    
    LB = arg[Q1] - (1.5 * IQR)
    UB = arg[Q3] + (1.5 * IQR)

    #print("OUTLIER <" + str(LB))
    #print(str(UB) + "< OUTLIER")
    return UB




print('Which areas take the longest time to dispatch to on average? How can this be reduced?')

fileName = "sfpd_dispatch_data_subset.csv"
df = pd.read_csv(fileName)

zc = df['zipcode_of_incident'] #stores the zipcode of each incident 
d0 = df['response_timestamp'] #stores when dispatched unit responds
d1 = df['on_scene_timestamp'] #stores when the dispatched unit arrives



parseZip = []
delta = []
y = []

for x in range(len(zc)): #casts the zipcodes to integers
    parseZip.append(int(zc[x]))
    
uniqueZip = []
for x in parseZip: #creates a list of unique zipcodes
    if x not in uniqueZip:
        uniqueZip.append(x)

date0 = pd.to_datetime(d0, format = "%Y-%m-%d %H:%M:%S.%f %Z")
date1 = pd.to_datetime(d1, format = "%Y-%m-%d %H:%M:%S.%f %Z")



zipSum = 0
zipCount = 0
output = {} #stores the avg response time for each zipcode
avg = [] #list of avg response times used to find the outliers


#this determines the average time for a unit to arrive to the incident
#at each unique zipcode

for a in range(len(uniqueZip)):
    #print(str(uniqueZip[a]) + '----------------------')    
    zipSum = 0
    zipCount = 0
    for x in range(10000):
        if parseZip[x] == uniqueZip[a]:
            temp = (date1[x] - date0[x]).total_seconds()/60.0
            if not math.isnan(temp) and temp != 0.0:
                #delta.append(round(temp,2))
                #print(round(temp,2))
                zipSum = zipSum + temp
                zipCount += 1
   
    #print('Average dispatch time: '+str(zipSum/zipCount))
    output.update({uniqueZip[a]: zipSum/zipCount})
    avg.append(zipSum/zipCount)
            
    
    
print('')
print('')
print("This a dictionary of each zipcode and its avg response time: ")
print(output)

print('')
print('')
print("These avg response times are outliers: ")
for x in avg:
    if x > outlier(avg):
        print(x)


print('')
print('')

print('Areas that take the longest time to dispatch on average:')
print('94134: 7.97 min')
print('94127: 10.36 min')
print('94130: 8.59 min')
print('94129: 9.57 min')





















