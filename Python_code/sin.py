#python code to plot sine plot

#import libraries
import matplotlib.pyplot as mpl
import numpy as np

#define function
def f(x):
   return np.sin(x)

#choose range to plot our result, 100 point is chosen to have smooth plot
x = np.linspace(-2*np.pi,2*np.pi,100)

#title of the graph
mpl.title('Sine graph')

#x axis label
mpl.xlabel('x')

#y axis label
mpl.ylabel('f(x)')

#plot x and y
mpl.plot(x,f(x))

#show the graph after executing python
mpl.show()
