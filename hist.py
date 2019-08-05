import numpy as np
import matplotlib.pyplot as plt

resultFile = "data/10tspResult.csv"
pathFile = "data/10all_path.csv"

if __name__ == "__main__":
    x = np.genfromtxt(resultFile, delimiter=",")
    x1 = np.genfromtxt(pathFile, delimiter=",")
    print(np.std(x1))
    print(np.average(x1))
    fig = plt.figure(figsize=[9, 9])
    ax = fig.add_subplot(211)
    ax.hist(x, bins=10, normed=False)
    ax.set_xlim(2.5, 6.5)
    ax.set_xlabel("Tour length")
    ax.set_ylabel("Frequency")
    ax = fig.add_subplot(212)
    ax.hist(x1, bins=100, color="orange", normed=False)
    ax.set_xlim(2.5, 6.5)
    ax.set_xlabel("Tour length")
    ax.set_ylabel("Frequency")
    # plt.show()
    plt.savefig("10city-compare.pdf", bbox_inches="tight", transparent=False)
