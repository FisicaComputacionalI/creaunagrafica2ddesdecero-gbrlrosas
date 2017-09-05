# lineplot.py
import numpy as np
import pylab as pl
# make an array of x values
x = [1,2,3,4]
# make an array of y values for each x value
y = [8,8,8,8]
# use pylab to plot x and y
pl.plot(x, y,'ro')
# show the plot on the screen
pl.savefig('promedio.png')
 
