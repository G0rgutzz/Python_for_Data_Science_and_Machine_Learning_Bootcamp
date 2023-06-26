import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 11)
y = x**2
'''
# functional method
plt.plot(x, y)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Y(X)') 
# multi plots
plt.subplot(1, 2, 1)  # number of rows, columns, plot number it refers to
plt.plot(x, y, 'r')
plt.subplot(1, 2, 2)
plt.plot(y, x, 'y')
plt.show()

# object oriented method
fig = plt.figure()
axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])  # left, bottom, width and height of the axis
axes.plot(x, y)
axes.set_xlabel('x')
axes.set_ylabel('y')
axes.set_title('Y(X)')
plt.show()

# multi index plot
fig = plt.figure()
axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])  # values need to be in (0, 1)
axes2 = fig.add_axes([0.2, 0.4, 0.7, 0.2])
axes1.plot(x, y)
axes1.set_title('Y(X)')
axes2.plot(y, x)
axes2.set_title('X(y)')
plt.show()

# object oriented method
# fig = plt.figure()
fig, axes = plt.subplots(nrows=1, ncols=2)
# axes.plot(x, y)
plt.tight_layout()  # bundles plot together, so they don't overlap
# for current_ax in axes:
#     current_ax.plot(x, y)
axes[0].plot(x, y)  # fills only mentioned plot - in this case 1st, same goes for titles etc
axes[1].plot(x, y*x)
plt.show()

# figure size, aspect ratio and dpi
# the same thing possible for subplots as above
fig = plt.figure(figsize=(5, 4), dpi=100)  # width and height of the figure in retarded units
ax = fig.add_axes([0.1, 0.1, 0.9, 0.9])
ax.plot(x, y*3, label='x^2')
ax.plot(x, y, label='x^3')

ax.legend(loc=(0.2, 0.3))  # requires labels in the related plots, loc=a location fo a legend, a is in <0, 10>
# or tupple as in location of the axes
plt.tight_layout()
plt.show()

# saving a plot
# fig.savefig('wykres1.png')  # dpi= is possible

'''
fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.9, 0.9])

ax.plot(x, y, color='#FF8C00', marker='*', markersize=15)  # name of the basic color or RGB code, linewidth possible, default=2
# alpha= describes transparency, linestyle= style of the line (dash, dotted etc)
# marker= gives exact location of the argument, markersize= size of the marker
# markerfacecolor= - color of the inside of the marker, markeredgewidth, markeredgecolor

# plot range
ax.set_xlim([-2, 7])
ax.set_ylim([-3, 10])
plt.show()

# special plot types
# plt.scatter(x, y)
# plt.hist(data)
# plt.boxplot(data, vert=True, patch_artist=True)
