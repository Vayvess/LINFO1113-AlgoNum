def trapezoid(f, a, b, i_old, k):
    if k == 1:
        i_new = (f(a) + f(b))*(b - a) * 0.5
    else:
        n = 2**(k - 2)
        h = (b - a)/n
        x = a + h/2.0
        sigma = 0.0
        for i in range(n):
            sigma += f(x)
            x += h
        i_new = (i_old + h * sigma) * 0.5
    return i_new
