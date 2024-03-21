import matplotlib.pyplot as plt
import numpy as np

from plastik import ridge


def r():
    # Data
    data = [
        (np.array([1, 2, 3]), np.array([6, 5, 7])),
        (np.array([2, 3, 4]), np.array([100, 1, -200])),
    ]
    lab = ["one", "two"]
    ridge.ridge_plot(data, "blank", "x_lim_S", "slalomaxis", "grid", "squeeze", labels=lab, lt="--", xlabel="XXX", ylabel="YYY")


if __name__ == "__main__":
    r()
    plt.show()
