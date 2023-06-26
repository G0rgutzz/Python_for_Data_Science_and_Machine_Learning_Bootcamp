import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 100)
y = x*2
z = x**2
'''
# exercise 1
fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.85, 0.85])
ax.plot(x, y)
ax.set_title('title')
ax.set_xlabel('x')
ax.set_ylabel('y')
# exercise 2 
fig = plt.figure()
ax1 = fig.add_axes([0.1, 0.1, 0.85, 0.85])
ax2 = fig.add_axes([0.2, 0.5, 0.2, 0.2])
ax1.plot(x, y)
ax2.plot(x, y)

# exercise 3
fig = plt.figure()
ax1 = fig.add_axes([0.1, 0.1, 0.85, 0.85])
ax2 = fig.add_axes([0.2, 0.5, 0.4, 0.4])
ax1.plot(x, z)
ax1.set_xlabel('x')
ax1.set_ylabel('z')
ax1.set_xlim([0, 100])
ax1.set_ylim([0, 10000])
ax2.plot(x, y)
ax2.set_title('zoom')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_xlim([20, 22])
ax2.set_ylim([30, 50])
plt.show()
'''
# exercise 4
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 6))
axes[0].plot(x, y, color='blue', linewidth=3, linestyle='--')
axes[1].plot(x, z, color='red', linewidth=3)
plt.tight_layout()
plt.show()
