
import os
import pandas as pd
import math
import numpy
import matplotlib.pyplot as plt

cwd = os.getcwd()
cwd

directory = "/Users/elizaveta/PycharmProjects/pythonProject/program_2/hw5/p.xlsx"

start = 1
finish = 3
count = 0.01


def exel(wereis, x, y):
    df = pd.DataFrame({"x": x, "y": y})
    df.to_excel(wereis)


def function_sin(start, finish, count):
    x = numpy.arange(start, finish, count)
    y = []
    for i in x:
        y.append(math.sin(i) + 0.1 * math.sin(i ** 5))
    return [x, y]


def smoothing(arr, k):
    res = []
    m = []
    for i in range(len(arr)):
        if i == 0:
            res.append(arr[i])
        else:
            window = arr[:i + 1]
            f = False
            while math.fabs((arr[i] - (sum(window) / len(window))) / arr[i]) > k:
                f = True
                if len(window) > 1:
                    window.pop(0)
                else:
                    break
            if f:
                m.append(len(window))
            res.append(sum(window) / len(window))
    return res


def mnk(x_dots, y_dots):
    n = len(x_dots)
    sum_x = sum(x_dots)
    sum_y = sum(y_dots)
    sum_xy = 0
    sum_x2 = 0
    for i in range(n):
        sum_xy += x_dots[i] * y_dots[i]
        sum_x2 += x_dots[i] ** 2
    a = (n * sum_xy - sum_y * sum_x) / (n * sum_x2 - sum_x ** 2)
    b = (sum_y - a * sum_x) / n
    return [a, b]


def line(x_1, y_1, x_2, y_2):
    k = (y_1 - y_2) / (x_1 - x_2)
    b = y_2 - k * x_2
    return [k, b]


x, y = function_sin(start, finish, count)
plt.plot(x, y)
y1 = smoothing(y, 0.1)
a, b = line(x[-2], y[-2], x[-1], y[-1])
x = list(x)
plt.plot(x, y1)
print("jhfg")
x.append(x[-1] + count)
y.append(x[-1] * a + b)
a, b = line(x[-3], y1[-2], x[-2], y1[-1])
y1.append(x[-1] * a + b)
plt.plot(x[-2:], y1[-2:], c="r")
plt.plot(x[-2:], y[-2:], c="g")
exel(directory, x, y)
plt.show()
