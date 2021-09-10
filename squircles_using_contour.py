import numpy as np
import matplotlib.pyplot as plt
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.contour.html?highlight=pyplot%20contour#matplotlib.pyplot.contour

r = 0.6
x = np.linspace(-1.1, 1.1, 100)
y = np.linspace(-1.1, 1.1, 100)
X, Y = np.meshgrid(x,y)
F = X**2 + Y**2 - r**2
# plt.contour(X,Y,F,[0])
# plt.axis('equal')
# plt.show()

a,b = 0,0
r = 1

x_value = list(x) 
y_value = list(x)
# grid
X, Y = np.meshgrid(x_value,y_value)

# Z values applied to grid
n = 7
F1 = abs(X)**n + abs(Y)**n - r**n
plt.contour(X,Y,F1,[0])

n = 2 # circle
F2 = abs(X)**n + abs(Y)**n - r**n
plt.contour(X,Y,F2,[0])

n = 1
F3 = abs(X)**n + abs(Y)**n - r**n
plt.contour(X,Y,F3,[0])
plt.axis('equal')
plt.show()

# imshow
fig, ax = plt.subplots()
# image function
ax.imshow(F2, origin='lower', interpolation='none')
#ax2=ax.twinx()
#ax2.contour(X,Y,F3,[0])

plt.axis('equal')
plt.show()

