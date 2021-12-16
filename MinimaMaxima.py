
import math


def minima_maxima(func, a, b, resolution=100, ignore_edges=True):
    '''
    Find the local minima and maxima of a function
    :param func: 1D function to search for the minima and maxima
    :param a: Begin of interval to search
    :param b: End of interval to search
    :param resolution: Number of points to take inbetween interval
    :param ignore_edges: Count edges of interval as local minima and maxima?
    :return: Minima and Maxima locations of the function
    '''
    points = [func(a + i * (b - a) / (resolution - 1)) for i in range(resolution)]
    maxima = []
    minima = []

    if not ignore_edges:
        if points[0] > points[1]:
            maxima.append(a)
        else:
            minima.append(a)

        if points[-1] > points[-2]:
            maxima.append(b)
        else:
            minima.append(b)

    upward_direction = points[0] < points[1]
    for index in range(resolution - 1):
        if upward_direction and points[index + 1] < points[index]:
            maxima.append(a + index * (b - a) / (resolution - 1))
            upward_direction = False

        if not upward_direction and points[index + 1] > points[index]:
            minima.append(a + index * (b - a) / (resolution - 1))
            upward_direction = True

    return minima, maxima


def test_func(theta):
    return abs(math.sin(theta))


if __name__ == "__main__":
    minima, maxima = minima_maxima(test_func, 0, 2 * math.pi, resolution=360, ignore_edges=False)
    print("abs(Sin()) from 0 to 2pi")
    print("Minimas [pi]:", [angle/math.pi for angle in minima])
    print("Maximas [pi]:", [angle/math.pi for angle in maxima])
