

from math import *
import matplotlib.pyplot as plt


def conv(impulse_response_list, signal_list):
    '''
    Convolves two lists of values
    :param impulse_response_func: Impulse response function with parameter
    :param signal_func: Input Signal function with parameter
    :return: List of convoluted values over time
    '''

    convolution = [0 for t in range(int(len(impulse_response_list) + len(signal_list) - 1))]

    for impulse_i in range(len(impulse_response_list)):
        for signal_i in range(len(signal_list)):
            convolution[impulse_i + signal_i] += impulse_response_list[impulse_i] * signal_list[signal_i]

    return convolution


def circular_convolution_lists(impulse_response_list, signal_list):
    lengths = [len(impulse_response_list), len(signal_list)]
    if lengths[1] > lengths[0]:
        short_list = impulse_response_list
        long_list = signal_list
    else:
        short_list = signal_list
        long_list = impulse_response_list

    convolution = [0 for i in range(int(max(lengths)))]

    for i in range(len(convolution)):
        for j in range(len(short_list)):
            convolution[i] += long_list[i - j] * short_list[j]

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


def sinc(x):
    '''
    It's the sinc function [sin(x) / x]
    :param x: Input x
    :return: Sinc function at x
    '''
    if x:
        return sin(x) / x
    return 1


def raised_cosine_filter(t, beta, T):
    '''
    Returns a digital raised cosine filter based on given beta and T
    :param t: Time input for the impulse response
    :param beta: Raised Cosine Roll-off Factor
    :param T: Reciprocal of the symbol rate (the period)
    :return: Impulse response at time 't'
    '''
    if not beta == 0 and (t == (T / 2 / beta) or t == -(T / 2 / beta)):
        return pi * sinc(pi / 2 / beta) / 4 / T
    return sinc(t * pi / T) * cos(pi * beta * t / T) / T / (1 - (2 * beta * t / T)**2)


def bit_stream(t_tot, t_delta, T, bits):
    bit_stream_out = [0 for t in range(int(t_tot / t_delta))]
    count = 0
    done = False
    for bit in bits:
        for i in range(int(count * T / t_delta), int((count + 1) * T / t_delta)):
            if i == len(bit_stream_out):
                done = True
                break
            bit_stream_out[i] = bit

        count += 1
        if done:
            break

    return bit_stream_out


def example_circular_convolution():
    signal = [2, 2]
    channel = [1, 1, -1]
    circular = circular_convolution_lists(signal, channel)
    print(circular)


def example_convolution():
    signal = [1, 1, 1, 1, 1, 1, 1, 1]
    channel = [1, 1, 1, 1, 1, 1, 1, 1]
    convolve = conv(signal, channel)
    print(convolve)


if __name__ == "__main__":
    example_convolution()




