import numpy as np
import least_square as lq

vx, vy = np.arange(9), np.array([3, 7, 15, 17, 31, 33, 39, 41, 63])
coefficients = lq.poly_fit(vx, vy, 3)
lq.plot_poly(vx, vy, coefficients)
