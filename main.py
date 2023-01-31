#importing libraries
import numpy as np
import matplotlib.pyplot as plt

#creating the dataset
data = {'C':20, 'C++':15, 'Java':30, 'Python': 35}

courses = list(data.keys())
values = list(data.values())

fig = plt.figure(figsize=(10,5))

#creating the bar plot
plt.bar(courses,values, color = 'red', width= 0.4)

#x and y values
plt.xlabel("Courses offered")
plt.ylabel("No. of students enrolled")

#the title
plt.title("Students enrolled in different courses")

#displaying the bar graph
plt.show()


