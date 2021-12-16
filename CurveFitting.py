
from math import *
import matplotlib.pyplot as plt


def least_squares(x, y=None):
    '''
    Least squares function for curve fitting. Helper functions in this module set up your x and y data to be curve fitted as specified
    :param x: x data
    :param y: y data
    :return: m, b (if not given linear data, will not fit correctly)
    '''

    if len(x) != len(y):
        print("ERROR: Least Squares: x and y are not the same length")
        return 0, 0

    if not isinstance(x, list):
        print("ERROR: Least Squares: x was not a list")
        return 0, 0

    if y is None:
        y = x
        x = [i for i in range(len(y))]
    else:
        if not isinstance(y, list):
            print("ERROR: Least Squares: y was not a list")
            return 0, 0

    N = len(x)

    sum_xy = sum(x[i] * y[i] for i in range(len(x)))
    sum_x = sum(x)
    sum_y = sum(y)
    sum_xsquared = sum(x[i]**2 for i in range(len(x)))

    m = (N * sum_xy - sum_x * sum_y) / (N * sum_xsquared - sum_x**2)
    b = (sum_y - m * sum_x) / N

    return m, b


def lin_fit(x, y=None):
    '''
    y = m * x + b
    :param x: x data points
    :param y: y data points
    :return: m, b
    '''
    if len(x) != len(y):
        print("ERROR: Lin Fit: x and y are not the same length")
        return 0, 0

    if not isinstance(x, list):
        print("ERROR: Lin Fit: x was not a list")
        return 0, 0

    if y is None:
        y = x
        x = [i for i in range(len(y))]
    else:
        if not isinstance(y, list):
            print("ERROR: Lin Fit: y was not a list")
            return 0, 0

    m, b = least_squares(x, y)
    return m, b


def log_fit(x, y=None):
    '''
    y = m * ln(x) + b
    :param x: x data
    :param y: y data
    :return: m, b
    '''
    if len(x) != len(y):
        print("ERROR: Log Fit: x and y are not the same length")
        return 0, 0

    if not isinstance(x, list):
        print("ERROR: Log Fit: x was not a list")
        return 0, 0

    if y is None:
        y = x
        x = [i for i in range(len(y))]
    else:
        if not isinstance(y, list):
            print("ERROR: Log Fit: y was not a list")
            return 0, 0

    m, b = least_squares([log(x_) for x_ in x], y)
    return m, b


def exp_fit(x, y=None):
    '''
    y = b * exp(m * x)
    :param x: x data
    :param y: y data
    :return: m, b
    '''
    if len(x) != len(y):
        print("ERROR: Exp Fit: x and y are not the same length")
        return 0, 0

    if not isinstance(x, list):
        print("ERROR: Exp Fit: x was not a list")
        return 0, 0

    if y is None:
        y = x
        x = [i for i in range(len(y))]
    else:
        if not isinstance(y, list):
            print("ERROR: Exp Fit: y was not a list")
            return 0, 0

    m, b = least_squares(x, [log(y_) for y_ in y])
    return m, exp(b)


def pow_fit(x, y=None):
    '''
    y = b * (x ^ m)
    :param x: x data
    :param y: y data
    :return: m, b
    '''
    if len(x) != len(y):
        print("ERROR: Pow Fit: x and y are not the same length")
        return 0, 0

    if not isinstance(x, list):
        print("ERROR: Pow Fit: x was not a list")
        return 0, 0

    if y is None:
        y = x
        x = [i for i in range(len(y))]
    else:
        if not isinstance(y, list):
            print("ERROR: Pow Fit: y was not a list")
            return 0, 0

    m, b = least_squares([log(x_) for x_ in x], [log(y_) for y_ in y])
    return m, exp(b)


if __name__ == "__main__":
    #  Lin fit
    #  y = m * x + b
    x_lin = [1, 2, 3, 4, 5]
    y_lin = [2, 5, 7, 7, 10]

    m, b = lin_fit(x_lin, y_lin)

    plt.plot(x_lin, y_lin, 'o')
    plt.plot(x_lin, [m * x + b for x in x_lin])
    plt.grid()
    plt.title("Linear Fit")
    plt.show()

    #  Log fit
    #  y = m * ln(x) + b
    x_log = [1, 4, 9, 16]
    y_log = [1, 2.5, 3.5, 5]

    m, b = log_fit(x_log, y_log)

    x_log_test = [i + 1 for i in range(19)]
    y_log_test = [m * log(x) + b for x in x_log_test]

    plt.plot(x_log, y_log, 'o')
    plt.plot(x_log_test, y_log_test)
    plt.grid()
    plt.title("Logarithmic Fit")
    plt.show()

    #  Exp fit
    #  y = b * exp(m * x)
    x_exp = [0, 1, 2, 3, 4]
    y_exp = [1, 3, 8, 15, 35]

    m, b = exp_fit(x_exp, y_exp)

    x_exp_test = [i/10 for i in range(40 + 1)]
    y_exp_test = [b * exp(m * x) for x in x_exp_test]

    plt.plot(x_exp, y_exp, 'o')
    plt.plot(x_exp_test, y_exp_test)
    plt.grid()
    plt.title("Exponential Fit")
    plt.show()

    #  Pow fit
    #  y = b * (x ^ m)
    x_pow = [1, 2, 3, 4]
    y_pow = [2, 8, 16, 32]

    m, b = pow_fit(x_pow, y_pow)

    x_pow_test = [i / 10 for i in range(40 + 1)]
    y_pow_test = [b * x**m for x in x_pow_test]

    plt.plot(x_pow, y_pow, 'o')
    plt.plot(x_pow_test, y_pow_test)
    plt.grid()
    plt.title("Power Fit")
    plt.show()







