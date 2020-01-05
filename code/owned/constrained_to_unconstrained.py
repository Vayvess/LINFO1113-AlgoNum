import numpy as np


def transform_constrained_to_unconstrained_problem(f, equality_constraints_functions, inequality_constraints_functions):
    def new_merit_func(x, lam):
        def penalty():
            sigma_g, sigma_h = 0, 0
            for g_function in equality_constraints_functions:
                sigma_g += np.power(g_function(x), 2)
            for h_function in inequality_constraints_functions:
                sigma_g += max(0, np.power(h_function(x), 2))
            return sigma_g + sigma_h
        return f(x) + lam * penalty()
    return new_merit_func


# The function we try to maximize
def func(x, y):
    # f(x, y) = x * y
    return x * y


# One of the equality constraints of func is x + y = 10
def equality_constraint_of_func(x):
    # this means that y = 10 - x
    return 10 - x


equality_constraints_of_func = [equality_constraint_of_func]  # can contain much more equalities constraints
inequality_constraints_of_func = []  # no inequalities constraints are given for this problem :)
new_merit_function_of_func = transform_constrained_to_unconstrained_problem(func,
                                                                            equality_constraints_of_func,
                                                                            inequality_constraints_of_func)


# I can now use 'new_merit_function_of_func' in an unconstrained algorithm as the merit function
# as new_merit_function_of_func(x_to_be_evaluated, multiplier_of_the_penalty
