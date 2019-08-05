import numpy as np
import matplotlib.pyplot as plt

resultFile = "data/15tspResult.csv"

if __name__ == "__main__":
    x = np.genfromtxt(resultFile, delimiter=",")
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    # ax.hist(x, bins=8, normed=True)
    binnum = 10
    ax.hist(x, color="orange", normed=False, bins=binnum)
    # ax_yticklocs = ax.yaxis.get_ticklocs()  # 目盛りの情報を取得
    # ax_yticklocs = list(map(lambda y: y * 1.0 / binnum, ax_yticklocs))  # 元の目盛りの値にbinの幅を掛ける
    # ax.yaxis.set_ticklabels(list(map(lambda y: "%0.2f" % y, ax_yticklocs)))
    # # 直した目盛りを表示
    ax.set_title("")
    ax.set_xlabel("Tour length")
    ax.set_ylabel("Frequency")
    plt.show()
    # plt.savefig('demo.png', transparent=True)
