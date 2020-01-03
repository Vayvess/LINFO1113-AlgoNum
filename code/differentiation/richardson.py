import numpy as np


# I got nothing for now
def richardson_extra(g, p, h=0.64):
    pass


def fun(x):
    return np.power(np.e, -x)


print(richardson_extra(fun, 3))
print(fun(0.64))
