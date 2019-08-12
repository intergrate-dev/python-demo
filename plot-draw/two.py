import matplotlib.pyplot as plot

if __name__ == "__main__":
    
    x_list_1 = [51.356515, 99.134178, 99.134178, 51.356515, 51.356515]
    y_list_1 = [50.346420, 50.346420, 41.454965, 41.454965, 50.346420]

    x_list_2 = [99.134178, 51.356515, 48.493434, 27.557154, 27.557154, 48.493434, 51.356515, 99.134178, 99.134178]
    y_list_2 = [70.207852, 70.207852, 70.207852, 70.207852, 59.468822, 59.468822, 51.385681, 51.385681, 70.207852]

    x_list_3 = [0.894713, 24.694073, 24.694073, 0.894713, 0.894713]
    y_list_3 = [81.639723, 81.639723, 58.660508, 58.660508, 81.639723]

    plot.figure('Line fig')
    ax = plot.gca()
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.plot(x_list_1, y_list_1, color='r', linewidth=1, alpha=1)
    ax.plot(x_list_2, y_list_2, color='g', linewidth=1, alpha=1)
    ax.plot(x_list_3, y_list_3, color='b', linewidth=1, alpha=1)
    plot.show()

    