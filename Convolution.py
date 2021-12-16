

from math import *
import matplotlib.pyplot as plt


def convolution(impulse_response_func, signal_func, t_tot=10, t_delta=0.1):
    '''
    Given two functions with parameter 't' for time, returns a list of values representing the
    signal response over time
    :param impulse_response_func: Impulse response function with parameter 't' for time
    :param signal_func: Input Signal function with parameter 't' for time
    :param t_tot: Total time to convolute over
    :param t_delta: Delta time between discrete points in time (d_Tau)
    :return: List of convoluted values over time
    '''
    impulse_reponse_vals = [impulse_response_func(t * t_delta) for t in range(int(t_tot/t_delta))]
    signal_vals = [signal_func(t * t_delta) for t in range(int(t_tot/t_delta))]
    convolution = [0 for t in range(int(t_tot/t_delta))]

    area = 0
    for num_points_to_use in range(int(t_tot/t_delta)):
        for index in range(num_points_to_use + 1):
            area = area + signal_vals[index] * impulse_reponse_vals[num_points_to_use - index] * t_delta
        convolution[num_points_to_use] = area
        area = 0

    return convolution


def test_rect(t):
    '''
    Example rectangle function to show off convolution function
    :param t: Time input for the signal
    :return: The value of the function at 't'
    '''
    if 0 < t <= 2:
        return 1
    return 0


def test_decay(t):
    '''
    Example exponential decay function to show off convolution function
    :param t: Time input for the signal
    :return: The value of the function at 't'
    '''
    return exp(-t)


if __name__ == "__main__":
    t_tot = 10
    t_delta = 0.1
    times = [t * 0.1 for t in range(int(t_tot/t_delta))]

    plt.plot(times, [test_rect(t * t_delta) for t in range(int(t_tot/t_delta))])
    plt.plot(times, convolution(test_rect, test_rect, t_tot=t_tot, t_delta=t_delta))
    plt.legend(["Signal/Impulse Response", "Convolution"])
    plt.show()

    plt.plot(times, [test_rect(t * t_delta) for t in range(int(t_tot/t_delta))])
    plt.plot(times, [test_decay(t * t_delta) for t in range(int(t_tot/t_delta))])
    plt.plot(times, convolution(test_rect, test_decay, t_tot=t_tot, t_delta=t_delta))
    plt.legend(["Signal", "Impulse Response", "Convolution"])
    plt.show()
