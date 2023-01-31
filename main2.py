#importing libraries
import numpy as np
import matplotlib.pyplot as plt

#setting up the dataset
y = np.array([35,25,25,15])
mylablels = ["Apples", "Bananas", "Cherries","Grapes"]
myexplode = [0.2,0,0,0]

plt.pie(y, lables = mylables, explode = myexplode, shadow = True)

#displaying the legend
plt.legend(title= "Four Fruits:")


#displaying the pie chart
plt.show()


