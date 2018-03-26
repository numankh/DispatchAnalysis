import pandas as pd
import matplotlib.pyplot as plt
import math


def average(arg): #calculates the average of a list 
    total = 0
    for x in range(len(arg)):
        if not math.isnan(arg[x]):
            total += arg[x]
            
    return total/len(arg)
 
    
def standard_deviation(arg): #calculates the standard deviation of a list 
    num = len(arg)
    total = 0
    for x in range(len(arg)):
        if not math.isnan(arg[x]):
            total += arg[x]     
        
    if num < 2:     #if the list is shorter than 2
                    #then the stdv cannot be found
        return None
    else:
        sumavg = 0
        for x in range(len(arg)):
            if not math.isnan(arg[x]):
                sumavg = sumavg + ((arg[x] - (total/num)) ** 2)
        return (sumavg/(num-1))**.5     #returns the stdv
    
    
fileName = "sfpd_dispatch_data_subset.csv"

df = pd.read_csv(fileName)
d0 = df['response_timestamp'] #stores the timestamp when the dispatched unit is leaving for the location of the incident 
d1 = df['on_scene_timestamp'] #stores the timestamp when dispatched unit arrives to the lcoation of the incident


delta = []
y = []

#parses the timestamps
date0 = pd.to_datetime(d0, format = "%Y-%m-%d %H:%M:%S.%f %Z")
date1 = pd.to_datetime(d1, format = "%Y-%m-%d %H:%M:%S.%f %Z")


#creates a new list that is the difference between the timestammps
for x in range(len(d1)):
    #delta.append(date1[x] - date0[x])
    delta.append((date1[x] - date0[x]).total_seconds()/60.0)


#creates the plot of the day of the incident vs the difference in timestamps
plt.plot(date0,delta,'ob')
plt.xticks(rotation=90)
plt.xlabel('Dates of 911 Calls')
plt.ylabel('Amount of Time a Dispatch Unit Reaches a Location (min)')
plt.title('Time Series Plot: Time Dispatch Unit Reaches Location')
plt.axis(["2018-01-13","2018-01-25", 0 ,60])
plt.grid(True)
plt.show()


print("Average: " + str(average(delta)))
print("Standard Deviation: " + str(standard_deviation(delta)))












