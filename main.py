import numpy as np
import matplotlib.pyplot as plt

data = {'C':20, 'C++':15, 'Java':30, 'Python': 35}

courses = list(data.keys())
values = list(data.values())

fig = plt.figure(figsize=(10,5))

plt.bar(courses,values, color = 'red', width= 0.4)

plt.xlabel("Courses")
plt.ylabel("No. of Students")

plt.show()