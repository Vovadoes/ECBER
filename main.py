import math

# from Charts import *


# from scipy.stats import t

# CONST
pi = 3.14159265
Yc = 17.3 * (10 ** -6)


def myround(x: float, lst: list):
    for i in lst:
        if x < i:
            return i
    return lst[-1]


class Calculation:
    def __init__(self, j, m):
        self.i_ef = (pow(1 + (j / (100 * m)), m) - 1) * 100
        pass


if __name__ == "__main__":
    j = 24
    m = 4
    calculation = Calculation(j, m )
    print(calculation.i_ef)
    # ChartLinePLT(calculation.chart_v_y_data)
    # plt.legend()
    # plt.show()
