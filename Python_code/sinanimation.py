#python code to plot sine plot

#import libraries
import matplotlib.pyplot as mpl
from matplotlib.animation import FuncAnimation
import numpy as np

#create the frame for animation
fig, ax = mpl.subplots()
xdata,ydata=[],[]
line, = ax.plot([],[],'bo')

#x axis label
mpl.xlabel('x')

#y axis label
mpl.ylabel('f(x)')

def init():
   ax.set_xlim(-2*np.pi,2*np.pi)
   ax.set_ylim(-1,1)
   return line,

#update the frame
def update(frame):
    xdata.append(frame)
    ydata.append(np.sin(frame))
    line.set_data(xdata, ydata)
    return line,
    
ani = FuncAnimation(fig, update, frames=np.linspace(-2*np.pi, 2*np.pi, 100),
                    init_func=init, blit=True)

ani.save('sine.gif', writer="pillow", fps=50)
#show the graph after executing python
mpl.show()
