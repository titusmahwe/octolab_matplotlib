import matplotlib.pyplot as plt 
import numpy as np

'''This is a basic matplotlib sketch diagram'''
x_axis = np.array([1,2,3,4,5])
y_axis = np.array([2,4,6,8,10])

plt.xlabel('x axis')
plt.ylabel('y axis')
plt.plot(x_axis, y_axis)
plt.show()
