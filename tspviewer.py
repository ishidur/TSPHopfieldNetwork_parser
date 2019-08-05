import numpy as np
import matplotlib.pyplot as plt

cityFile = "./data/10cities.csv"
cities = np.genfromtxt(cityFile, delimiter=",")
route = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# route = [0, 1, 2, 3, 4, 5, 6, 8, 7, 9, 0]
if __name__ == "__main__":
    x = []
    y = []
    for city in route:
        x.append(cities[city][0])
        y.append(cities[city][1])
    # for city in cities:
    #     x.append(city[0])
    #     y.append(city[1])
    fig = plt.subplots(num=None, figsize=(8, 8), dpi=120, facecolor="w", edgecolor="k")
    plt.plot(x, y, "o-")
    plt.xlim(0.0, 1.0)
    plt.ylim(0.0, 1.0)
    plt.grid()
    # plt.show()
    # plt.savefig('plotname.png', bbox_inches='tight', transparent=False)
    plt.savefig("plotname.pdf", bbox_inches="tight", transparent=False)
