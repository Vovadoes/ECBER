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
    def __init__(self, i, j, m1, m2):
        self.i = i
        self.j = j
        self.m1 = m1
        self.m2 = m2
        self.result = None
        self.flag = None

    def iffect(self):
        self.result = (pow(1 + (self.j / (100 * self.m1)), self.m1) - 1) * 100
        self.flag = True

    def base(self):
        self.result = self.m2 * (pow(1 + self.i / 100, 1 / self.m2) - 1) * 100
        self.flag = False


if __name__ == "__main__":
    j = 24
    m1 = 4
    i = 25
    m2 = 12
    calculation = Calculation(i, j, m1, m2)
    calculation.iffect()
    print(calculation.result)
    calculation.base()
    print(calculation.result)
    # ChartLinePLT(calculation.chart_v_y_data)
    # plt.legend()
    # plt.show()
