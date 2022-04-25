# апроксимация
import random
import matplotlib.pyplot as plt

arr = []
n = random.randint(500, 1000)
for i in range(n):
    arr.append(random.randint(1, 100))
indexes = [i for i in range(n)]
del_dots = {}
for i in range(30):
    index = random.choice(indexes)
    arr[index] = random.randint(200, 400)
    del_dots[index] = arr[index]

arr_2 = arr[:]


def sigma(arr):
    summ = sum(arr)
    n = len(arr)
    medium = summ // n
    s = 0
    for i in arr:
        s += (i - medium) ** 2
    s = (s / (n - 1)) ** 0.5
    return s * 3


def approx(x):
    y = [i for i in range(len(arr))]
    summ_x = sum(x)
    summ_y = sum(y)
    summ_x2 = 0
    summ_xy = 0
    for i in range(len(x)):
        summ_x2 += x[i] ** 2
        summ_xy += x[i] * i
    a = (len(x) * summ_xy - summ_x * summ_y) / (len(x) * summ_x2 - summ_x ** 2)
    b = (summ_y - a * summ_x) / n
    return [a, b]


def graf(graff, arr, del_dots, new_dots):
    del_x = list(del_dots.keys())
    del_y = list(del_dots.values())
    new_x = list(new_dots.keys())
    new_y = list(new_dots.values())
    y = [i for i in range(len(arr))]
    a = [i for i in range(len(graff))]
    plt.plot(a, graff)
    plt.scatter(y, arr)
    plt.scatter(del_x, del_y, c="r")
    plt.scatter(new_x, new_y, c="#00FF00")
    plt.show()


a, b = approx(arr)
sss = sigma(arr)
new_dots = {}
for i in range(len(arr)):
    if arr[i] > sss:
        arr[i] = a * i + b
        new_dots[i] = arr[i]
n = len(arr)
graff = []
for i in range(n):
    graff.append(a * i + b)


def line(x_1, y_1, x_2, y_2):
    k = (y_1 - y_2) / (x_1 - x_2)
    b = y_2 - k * x_2
    return (k, b)


new = {}

for i in range(len(arr_2)):
    if arr_2[i] > sss:
        if i == 0:
            key = i + 1
            if arr_2[key] > sss:
                while arr_2[key] > sss:
                    key += 1
            key_2 = key + 1
            if arr_2[key_2] > sss:
                while arr_2[key_2] > sss:
                    key_2 += 1
        elif i == len(arr_2):
            key = i - 1
            if arr_2[key] > sss:
                while arr_2[key] > sss:
                    key -= 1
            key_2 = key - 1
            if arr_2[key_2] > sss:
                while arr_2[key_2] > sss:
                    key_2 -= 1
        else:
            key = i - 1
            if arr_2[key] > sss:
                while arr_2[key] > sss:
                    key -= 1
            key_2 = i + 1
            if arr_2[key_2] > sss:
                while arr_2[key_2] > sss:
                    key_2 += 1
        a, b = line(key, arr_2[key], key_2, arr_2[key_2])
        arr_2[i] = a * i + b
        new[i] = arr_2[i]
plt.plot(indexes, arr_2)
plt.scatter(list(del_dots.keys()), list(del_dots.values()), c="r")
plt.scatter(list(new.keys()), list(new.values()), c="#00FF00")
plt.show()
