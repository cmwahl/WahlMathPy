
from cmath import *
import matplotlib.pyplot as plt


def fourier_transform(data, t_delta, freq=-1, freq_res=100):
    '''
    Return the Fourier Transform of the data. If freq is given, compute the Fourier Transform
    for that given frequency. If not given, compute an a Fourier Transform from 0 to 1 / 2 / t_delta
    :param data: Data points to transform
    :param t_delta: Time difference between points in data
    :param freq: If given a frequency(ies) [as a list] to compute, will calculate the FT at that value
    :param freq_res: If freq=-1, the number of frequencies to use with the FT of data
    :return: Fourier Transform of the data, and the frequencies used
    '''

    if not freq == -1 and not isinstance(freq, list) and not isinstance(freq, tuple):
        return sum([data[i] * exp(1j * 2 * pi * freq * t_delta * i) / len(data) for i in range(len(data))]), freq

    max_freq = 0.5 / t_delta
    if freq == -1:
        frequencies = [freq * max_freq / (freq_res - 1) for freq in range(freq_res)]
    else:
        frequencies = freq

    FT = [0 for freq in range(len(frequencies))]

    for i in range(len(frequencies)):  # For every frequency
        for k in range(len(data)):  # Calculate the FT through all the data
            FT[i] += data[k] * exp(1j * 2 * pi * frequencies[i] * t_delta * k)
        FT[i] /= len(data)

    return FT, frequencies


if __name__ == "__main__":
    time = 50
    t_delta = .01
    data = [cos(2 * pi * t * t_delta) + cos(2 * pi * t * t_delta * 3) for t in range(int(time / t_delta + 1))]
    print("FT at freq = 1Hz:", fourier_transform(data, t_delta, freq=1))

    max_freq = 10
    freq_res = .1
    frequencies = [i * freq_res for i in range(int(max_freq / freq_res + 1))]
    ft, freqs = fourier_transform(data, t_delta, frequencies)

    plt.plot(freqs, ft)
    plt.grid()
    plt.show()


