#python code to plot sine plot
#import libraries
import matplotlib.pyplot as mpl
import numpy as np

#define function for sin
def f(x):
   return np.sin(x)
   
#define function for cos
def g(x):
   return np.cos(x)

#choose range to plot our result, 100 point is chosen to have smooth plot
x = np.linspace(-2*np.pi,2*np.pi,100)

#title of the graph
mpl.title('Sine and Cosine graph')

#x axis label
mpl.xlabel('x')

#y axis label
mpl.ylabel('f(x)')

#plot x and y
mpl.plot(x,f(x))
mpl.plot(x,g(x))

#show the graph after executing python
mpl.show()
