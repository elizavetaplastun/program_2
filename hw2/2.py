import random

import matplotlib.pyplot as plt

n = int(input())
matrix = [[0 for i in range(n)] for i in range(n)]
for arr in matrix:
    for i in range(n):
        arr[i] = random.randint(1, 30)

print(matrix)


def index_for_del(l):
    matrix = {}
    for i in range(l):
        random_index_x = random.randint(0, n - 1)
        random_index_y = random.randint(0, n - 1)
        while True:
            if random_index_x not in matrix.keys():
                matrix[random_index_x] = []
                matrix[random_index_x].append(random_index_y)
                break
            elif random_index_y in matrix[random_index_x]:
                random_index_y = random.randint(0, n - 1)
            else:
                matrix[random_index_x].append(random_index_y)
                break
    indexes = list(matrix.keys())
    answer = {}
    indexes.sort()
    for i in indexes:
        answer[i] = matrix[i]
        answer[i].sort()
    return answer


random_matrix = index_for_del(10)


def del_random(matrix, random_matrix):
    for i in random_matrix.keys():
        for j in random_matrix[i]:
            matrix[i][j] = 0


del_random(matrix, random_matrix)
x_coordinats = [i for i in range(n ** 2)]
print(matrix)
xy = {}
key = -1
for i in range(n):
    for j in range(n):
        key += 1
        xy[x_coordinats[key]] = matrix[i][j]

x = []
y = []
for i in xy:
    if xy[i] != 0:
        x.append(i)
        y.append(xy[i])


def graf(a, b, x, y, del_dots):
    del_x = list(del_dots.keys())
    del_y = list(del_dots.values())
    plt.plot(a, b)
    plt.scatter(x, y)
    plt.scatter(del_x, del_y, c="r")
    plt.show()


def axb(x, y):
    xy = []
    x2 = []
    for i in range(len(x)):
        xy.append(x[i] * y[i])
        x2.append(x[i] ** 2)
    summ_x = sum(x)
    summ_y = sum(y)
    summ_xy = sum(xy)
    n = len(x)
    a = (n * summ_xy - summ_x * summ_y) / (n * summ_y - summ_x ** 2)
    b = (summ_y - a * summ_x) / n
    return [a, b]


a, b = axb(x, y)
del_dots = {}
print(f" прямая - y={a}x+{b}")
y_coordinates = []
x_coordinats = []
for i in range(n ** 2):
    y_coordinates.append(a * i + b)
    x_coordinats.append(i)
k = list(xy.values())
key = -1
for i in range(n):
    for j in range(n):
        key += 1
        if xy[key] == 0:
            matrix[i][j] = a * key + b
            del_dots[key] = a * key + b
graf(x_coordinats, y_coordinates, x_coordinats, k, del_dots)
print(matrix)
