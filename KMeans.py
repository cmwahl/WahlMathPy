
import CSV
import random as rand
import matplotlib.pyplot as plt

def __find_dist(loc1, loc2):
    tot = 0
    for i in range(len(loc1)):
        tot = tot + (loc1[i] - loc2[i])**2

    return tot**0.5


def __find_avg_loc(indices, data_points):
    #  Sum up coords
    tots = [0 for i in range(len(data_points[0]))]
    for index in indices:
        for coord in range(len(tots)):
            tots[coord] = tots[coord] + data_points[index][coord]

    #  Average out coords
    for coord in range(len(tots)):
        tots[coord] = tots[coord] / len(indices)

    return tots


def kMeans(k, data_points):
    cols = len(data_points)
    rows = len(data_points[0])

    min_dims = [min(data_points[col]) for col in range(cols)]
    max_dims = [max(data_points[col]) for col in range(cols)]

    clusters = [{"id": i, "indices": [], "loc": [rand.uniform(min_dims[j], max_dims[j]) for j in range(cols)]} for i in range(k)]

    data_points = __column2row(data_points)

    counter = 0
    while True:
        #  print(counter)

        counter = counter + 1
        #  Iterate through points and assign to closest cluster
        for point in range(rows):
            #  Check the first cluster, then check the rest
            dist = __find_dist(data_points[point], clusters[0]["loc"])
            id = 0
            for cluster in range(1, k):
                new_dist = __find_dist(data_points[point], clusters[cluster]["loc"])
                if dist > new_dist:
                    id = cluster
                    dist = new_dist
            clusters[id]['indices'].append(point)

        #  Update cluster locations
        update = False
        for cluster in clusters:
            if len(cluster['indices']) > 0:
                new_loc = __find_avg_loc(cluster['indices'], data_points)
                if not new_loc == cluster['loc']:
                    update = True
                    cluster['loc'] = new_loc

        if not update:
            break

        #  Reset
        for cluster in range(k):
            clusters[cluster]['indices'].clear()

    return clusters


def __column2row(data_points):
    cols = len(data_points)
    rows = len(data_points[0])

    return [[data_points[col][row] for col in range(cols)] for row in range(rows)]


def __row2column(data_points):
    cols = len(data_points[0])
    rows = len(data_points)

    print(cols, rows)
    return [[data_points[row][col] for row in range(rows)] for col in range(cols)]


if __name__ == "__main__":
    data_dir = "C:/Users/cmwah/PycharmProjects/WahlMath/kMeansTest.csv"
    data, names = CSV.read_csv(data_dir, separator="\t")

    print("Names:", names)
    print("Data:", data)

    #  Make our data points floats instead of strings
    for i in range(len(data)):
        for j in range(len(data[0])):
            data[i][j] = float(data[i][j])

    clusters = kMeans(3, data)
    print(clusters)

    colors = ['b', 'g', 'r']
    count = 0
    for cluster in range(len(clusters)):
        #  Plot points
        for point in clusters[cluster]['indices']:
            plt.scatter(data[0][point], data[1][point], c=colors[count], marker='o')
        #  Plot cluster loc
        plt.scatter(clusters[cluster]['loc'][0], clusters[cluster]['loc'][1], c=colors[count], marker='s')
        count = count + 1
    plt.title("Squares are cluster points, circles are data points, colors specify a group")
    plt.show()

