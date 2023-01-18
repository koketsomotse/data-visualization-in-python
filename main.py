#import matloptlib and numpy
import numpy as np
import matplotlib.pyplot as plt

#creating the dataset for the students
data = {'C': 20 , 'C++': 15, 'Java': 30, 'Python': 35}
courses = list(data.keys())
values = list(data.values())

fig = plt.figure(figsize=(10,5))

plt.bar(courses,values, color ="maroon", width= 0.4)

plt.xlabel("Course offered")
plt.ylabel("No. of students enrolled")

plt.title("xcv")

plt.show()