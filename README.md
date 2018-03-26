## Optimizing and Predicting Emergency Calls in San Francisco

The purpose of this project was to analyze and display trends in public data from the San Francisco Fire Department that contained dispatch information for emergency calls, with call time, location, dispatch. 


### Question 1

Data Visuals: Display or graph 3 metrics or trends from the data set that are interesting to you.

When looking at all of the dispatch data provided, I was interested in specifically analyzing the timestamp data. One of the goals for this project was optimization of the dipatch process. Therefore, I was eager to depict three trends that had to do with the amount of time different parts of the dispatch process took. The trends I looked into were the amount of time an operator takes to dispatch an emergency vehicle, the amount of time a unit takes from receiving a dispatch to arriving on scene, and the amount of time an ambulance takes to reach the nearest hospital.



<p align="center">
  <img src="911%20Operator%20Reaction%20Time.png">
</p>


Analyzing the data from this graph, the average of the reaction times of operators in San Francisco's Fire Department was 3.75 minutes. The standard deviation of this data was 20.18, in other words, the reaction times of 911 operators are extremely spread over a wide range. 


<p align="center">
  <img src="Dispatch%20Unit%20Drive%20Time.png">
</p>


Analyzing the data from this graph, the average time of the dispatched unit reaching the location of the incident was 4.63 minutes. The standard deviation of this data was 5.52, therefore, the amount of time vehicles to reach the location of the incident is much closer to the mean than the previous trend.


<p align="center">
  <img src="Ambulance%20Drive%20Time.png">
</p>


Analyzing the data from this graph, the average time of an ambulance reaching the nearest hospital was 4.44 minutes. The standard deviation of this data was 7.81, therefore, the amount of time ambulances took to reach the hospital was somewhat varied and away from the mean.

For further information on the data visuals, look at operatorTime.py, dispatchTime.py, or ambulanceTime.py.



### Question 2

Given an address and time, what is the most likely dispatch to be required?


Addressing this problem required properly understanding how to group data, store data, access data, and finally displaying it to the user. Essentially the user would enter an address such as "700 44TH AVE SF" and then enter a military-time such as "12". The script would the map of occurances of each type of call_type in a unique hour of the day which is in a unique zip code. The script then determines the most likely dispatch required and displays it to the user. Here is a sample run:

```markdown
Sample run of dispatchPredictor.py

Given an address and time, what is the most likely dispatch to be required?

Please enter an address (EX: 700 44TH AVE SF): 1700 CALIFORNIA ST SF

Please enter a time of day (0-23): 23

Most likely dispatch to be required: Medical Incident
```

### Question 3

Which areas take the longest time to dispatch to on average? How can this be reduced?


```markdown
# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image][src]


[src]: https://github.com/numankh/numankh.github.io/blob/master/Dispatch%20Unit%20Drive%20Time.png
```



For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/numankh/DispatchAnalysis/settings). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://help.github.com/categories/github-pages-basics/) or [contact support](https://github.com/contact) and we’ll help you sort it out.
