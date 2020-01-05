import numpy as np
import matplotlib.pyplot as plt


def analytical(x):
    return (31 / 32) * np.power(np.e, -4 * x) + (1 / 4) * x ** 2 - (1 / 8) * x + (1 / 32)


vx = np.arange(0, 10, 0.01)

print(1 + -4 * 0.01)
print(analytical(0.01))