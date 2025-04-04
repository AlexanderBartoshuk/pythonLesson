import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as data
import matplotlib.patches as mpatches
import matplotlib.lines as mlines

from matplotlib.legend_handler import HandlerLine2D , HandlerTuple

fig, ax = plt.subplots()
red_patch = mpatches.Patch(color='red', label = 'The red data')
ax.legend(handles=[red_patch])
plt.show()


fig,ax = plt.subplots()
blue_line = mlines.Line2D([], [], color='blue', marker='*',
                          markersize=15, label='Blue stars')
ax.legend(handles=[blue_line])
plt.show()


fig,axs = plt.subplot_mosaic([['left','right']], layout='constrained')

axs['left'].plot([1,2,3], label='test1')
axs['left'].plot([3,2,1], label='test2')

axs['right'].plot([1, 2, 3], 'C2', label="test3")
axs['right'].plot([3, 2, 1], 'C3', label="test4")

fig.legend(loc='outside upper right')


fig,ax = plt.subplots()
line1, = ax.plot([1,2,3], label='Line 1', linestyle='--')
line2, = ax.plot([3,2,1],label='Line 2', linewidth=4)

first_legend = ax.legend(handles=[line1], loc='upper right')
ax.add_artist(first_legend)
ax.legend(handles=[line2],loc='lower right')
plt.show()

fig,ax = plt.subplots()
line1, = ax.plot([3,2,1], marker='o', label = 'line1')
line2, = ax.plot([1,2,3], marker='o', label = 'line2')

ax.legend(handler_map={line1: HandlerLine2D(numpoints=4)}, handlelength=4)

fig, ax = plt.subplots()
p1, = ax.plot([1,2.5,3], 'r-d')
p2, = ax.plot([3,2,1],'k-o')

l = ax.legend([p1,p2], ['Two keys'], numpoints=1, handler_map={tuple:HandlerTuple(ndivide=None)})

