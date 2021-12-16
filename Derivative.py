from math import *


def derive(func, x, delta=0.001):
    '''
    Derives a function at a give point
    :param func: Function handle of function to derive
    :param x: Point to find derivative
    :param delta: Interval used to find derivative (smaller the better)
    :return: Derivative evaluated at x
    '''
    return (func(x + delta/2) - func(x - delta/2)) / delta


if __name__ == "__main__":
    print("Estimated Derivative:", derive(exp, 1))
    print("Actual Derivative:", exp(1))
