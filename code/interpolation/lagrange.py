import math
import numpy as np
import matplotlib.pyplot as plt


def lagrange(vx, vy, x):
    y, n = 0, len(vx)
    for i in range(n):
        prod = 1
        for j in range(n):
            if i != j:
                prod *= (x - vx[j]) / (vx[i] - vx[j])
        y += vy[i] * prod
    return y


x_data_set = np.array([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5], dtype='float')
y_data_set = np.array([25, 16, 9, 4, 1, 0, 1, 4, 9, 16, 25], dtype='float')


data_set = []
for px in np.arange(-5, 5, 0.1):
    data_set.append(lagrange(x_data_set, y_data_set, px))

plt.plot(np.arange(-5, 5, 0.1), data_set)

for i in range(100):
    print(i, lagrange(x_data_set, y_data_set, i))
plt.show()
