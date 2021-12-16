from math import *
import matplotlib.pyplot as plt


def semilogspace(start, end, resolution=100):
    '''
    Creates an x array of values even spaced across a logarithmic plot (normal plotting creates too many points at low values)
    :param start: Start value
    :param end: End value
    :param resolution: Points per decade
    :return:
    '''
    return [10 ** (i / resolution) for i in range(int(log10(start) * resolution), int(log10(end) * resolution + 1))]


if __name__ == "__main__":
    start_val = 10**7
    end_val = 5*(10**7)
    x = semilogspace(start_val, end_val)

    plt.loglog(x, x, 'o')
    plt.grid()
    plt.show()
