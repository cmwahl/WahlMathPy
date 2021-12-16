
import math


def find_zero(func, a, b, error=.001):
    '''
    Finds the zero of a given 1D function using Bisection Method (Zero must lie between a & b)
    :param func: Function to evaluate
    :param a: Beginning of interval to check for zero
    :param b: End of interval to check for zero
    :param error: Acceptable error from 0
    :return: If found, zero of function within error
    '''
    if a > b:
        a, b = b, a

    a_sign = func(a)/abs(func(a))
    b_sign = func(b)/abs(func(b))

    if a_sign * b_sign >= 0:
        print("ERROR: find_zero: Cannot confirm interval [a, b] contains a zero")
        return None

    while True:

        midpoint = (a + b) / 2

        if abs(func(midpoint)) < error:
            break

        if func(midpoint) * a_sign > 0:
            a = midpoint
        else:
            b = midpoint

    return midpoint


def test_func(x):
    return x + 2


if __name__ == "__main__":
    print(find_zero(test_func, 3, -5))

