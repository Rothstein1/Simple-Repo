# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 13:09:38 2023

@author: jacob
"""

##Most of the Matplotlib utilities lies under the pyplot submodule, and are usually imported under the plt alias
import matplotlib.pyplot as plt
from matplotlib.figure import Figure 
import numpy as np 

## Simple plot of two lists containing the X,Y coordinates for the plot 
## Line plot
# initializing the data
x = [10, 20, 30, 40]
y = [20, 30, 40, 50]

# plotting the data
plt.plot(x, y)

# Adding the title
plt.title("Simple Plot")

# Adding the labels
plt.ylabel("y-axis")
plt.xlabel("x-axis")
plt.show()


