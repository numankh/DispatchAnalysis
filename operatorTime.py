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
d0 = df['received_timestamp'] #stores the timestamp when operator received the 911 call
d1 = df['dispatch_timestamp'] #stores the timestamp when the operator dispatches a unit to the incident


delta = []

#parses the timestamp
date0 = pd.to_datetime(d0, format = "%Y-%m-%d %H:%M:%S.%f %Z")
date1 = pd.to_datetime(d1, format = "%Y-%m-%d %H:%M:%S.%f %Z")


#creates a new list that is the difference between the timestammps
for x in range(len(d1)):
    #delta.append(date1[x] - date0[x])
    delta.append((date1[x] - date0[x]).total_seconds()/60.0)


#creates the plot of the day of the incident vs the difference in timestamps
plt.plot(date0,delta,'og')
plt.xticks(rotation=90)
plt.xlabel('Dates of 911 Calls')
plt.ylabel('Reaction Time of Operator to Dispatch a Unit (min)')
plt.title('Time Series Plot: Reaction Time of 911 Operator')
plt.axis(["2018-01-13","2018-01-25", 0 ,100])
plt.grid(True)
plt.show()


print("Average: " + str(average(delta)))
print("Standard Deviation: " + str(standard_deviation(delta)))









