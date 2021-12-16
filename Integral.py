from math import *


def integrate(func, lower, upper, delta=0.01):
    '''
    Integrates a given function using trapezoid method
    :param func: A function of returning the mathematical function for integration
    :param lower: The lower bound for integration
    :param upper: The upper bound for integration
    :param delta: The steps for integration
    :return: The integrated value
    '''
    area = 0
    lower_step = lower

    while lower_step + delta < upper:
        area += (func(lower_step) + func(lower_step + delta)) * delta / 2
        lower_step += delta

    area += (func(lower_step) + func(upper)) * (upper - lower_step) / 2

    return area


if __name__ == "__main__":
    print("Estimated integral:", integrate(exp, 0, 1))
    print("Actual integral:", exp(1) - 1)
