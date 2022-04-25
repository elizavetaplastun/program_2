import matplotlib.pyplot as plt
import random


def one_more_stupid_function(x_dots, y_dots):
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


def random_arr(min_value, max_value, len_arr):
    arr = [min_value]
    for i in range(1, len_arr):
        a = random.randint(min_value, max_value)
        if a < arr[i - 1]:
            while a < arr[i-1]:
                a += random.randint(min_value, max_value)
        arr.append(a)
    return arr


def line(a, b, dots):
    n = len(dots)
    y = []
    for i in range(n):
        y.append(dots[i] * a + b)
    return y


n = 50
x = random_arr(2, 70, n)
y = random_arr(60, 300, n)
a, b = one_more_stupid_function(x, y)
y2 = line(a, b, x)
plt.scatter(x, y)
plt.plot(x, y2, c="r")
plt.show()
