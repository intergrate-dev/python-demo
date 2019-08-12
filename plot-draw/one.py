import matplotlib.pyplot as plt
# import random

if __name__ == '__main__':
    x1 = {"51.356515", "99.134178", "99.134178", "51.356515"},
    y1 = {"50.346420", "50.346420", "41.454965", "41.454965"}
    # x1 = list(range(10))
    # y1 = [random.randint(0, 10) for i in range(10)]
    plt.plot(x1, y1, color='r', markerfacecolor='blue', marker='o')
    for a, b in zip(x1, y1):
        plt.text(a, b, (a, b), ha='center', va='bottom', fontsize=10)

    plt.legend()
    plt.show()

