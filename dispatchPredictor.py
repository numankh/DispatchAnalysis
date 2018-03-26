# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 11:36:20 2018

@author: khann
"""



import pandas as pd
from geopy.geocoders import Nominatim


fileName = "sfpd_dispatch_data_subset.csv"
df = pd.read_csv(fileName)
d0 = df['location'] #stores the latitude and longitude of each incident


print('Given an address and time, what is the most likely dispatch to be required?')
address = input("Please enter an address (EX: 700 44TH AVE SF): ")
timeOfDay = input("Please enter a time of day (0-23): ")
print('')


timeOfDay = timeOfDay[0:2] #parses the time for the hour of day
timeOfDay = int(timeOfDay) 

geolocator = Nominatim() #this script takes the address the user enters
                         #and determines the latitude and longitude
                         #so that the full address can be obtained
                         
                         
temp = geolocator.geocode(address)
xyCoord = str(temp.latitude) +", "+ str(temp.longitude)
temp1 = geolocator.reverse(xyCoord)
parseForZip = temp1.address 

zipcode = 0
for y in range(len(parseForZip)): #this for loop finds the zipcode
    if parseForZip[y:y+3] == ', 9':
        zipcode = int(parseForZip[y+2:y+7]) 
        
        


zc = df['zipcode_of_incident'] #stores the zipcodes 
ct = df['call_type'] #stores the call_types 
rt = df['received_timestamp'] #stores the initial timestamp of the 911 call



parseTime = pd.to_datetime(rt, format = "%Y-%m-%d %H:%M:%S.%f %Z")
time = []

#this extracts the hour of day from the time when the 911 call was made
for x in range(len(parseTime)): 
    time.append(int(str(parseTime[x])[11:13]))
    
#this is a generic list of all the hours in a military clock
militaryTime = []
for x in range(24):
    militaryTime.append(x)
    



parseZip = []
for x in range(len(zc)): #this converts all the zipcodes into integers
    parseZip.append(int(zc[x]))
    
uniqueZip = []
for x in parseZip: #this determines the unique zipcodes from the data
    if x not in uniqueZip:
        uniqueZip.append(x)

uniqueZip = sorted(uniqueZip)





dispatchType = {}
times = {}
output = {}



#this part of the code creates a zipcode map of an hour map of a number of
#incident occurances for each call type map

for x in range(len(uniqueZip)): #loops through the unique zipcodes
    times = {}
    for t in militaryTime: #loops through the hours in a military day
        dispatchType = {}
        for line in range(10000): #loops through the entire data set
            if militaryTime[t] == time[line] and uniqueZip[x] == zc[line]:
                if(ct[line] not in dispatchType.keys()):
                    dispatchType.update({ct[line]:1})
                else:
                    count = dispatchType[ct[line]]
                    dispatchType.update({ct[line]:count+1})
                    
        times.update({militaryTime[t]:dispatchType})
    output.update({uniqueZip[x]:times})


    
#this takes the address and time of day the user entered to determine the 
#most likely call type that would be required 
max = 0
maxCallType = ""
for keys in output[zipcode][timeOfDay].keys():
    if output[zipcode][timeOfDay][keys] > max:
        max = output[zipcode][timeOfDay][keys]
        maxCallType = keys

print("Most likely dispatch to be required: " + maxCallType)
        
        
    

