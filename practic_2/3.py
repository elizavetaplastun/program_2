import random
import numpy as np


def rand_delete(array, value):
    delete_x = []
    delete_y = []
    for i in range(10):
        while True:
            x = random.randint(0, len(array) - 1)
            y = random.randint(0, len(array) - 1)
            if array[y][x] != value: break
        delete_x.append(len(array) * y + x)
        delete_y.append(array[y][x])
        array[y][x] = value
    return (delete_x, delete_y)


def correlation(array):
    print("YOUR MATRIX: \n")
    rand_delete(array, 0)
    Print(array)
    print("\n")
    data = []
    while len(array) > 0:
        data.append([array.pop(), []])

    for i in range(len(data)):
        for j in range(len(data)):
            if i != j:
                a = np.array(data[i][0])
                b = np.array(data[j][0])
                if sum(data[j][0]) == 0:
                    data[i][1].append([0, j])
                else:
                    data[i][1].append([np.corrcoef(a, b).max(), j])
        data[i][1].sort()

    while full_recover(data):
        for i in data: recover_correlation(i, data)
    for i in range(len(data)):  data[i] = data[i][0]
    return data


def recover_correlation(row, data):
    deleten = []
    for i in range(len(row[0])):
        if row[0][i] == 0: deleten.append(i)

    for i in range(len(row[1])):
        for j in range(len(deleten)):
            if deleten[j] == None: continue
            row_index = row[1][i][1]
            element = data[row_index][0][deleten[j]]
            if element != 0:
                row[0][deleten[j]] = data[row[1][i][1]][0][deleten[j]]
                deleten[j] = None


def full_recover(data):
    for row in data:
        if 0 in row[0]: return True
    return False


# красивый вывод
def Print(data):
    col_width = max(word for row in data for word in row)
    for row in data:
        print(" ".join(str(word).ljust(len(str(col_width))) for word in row))


def rand(length):
    result = []
    count = 1
    for i in range(length):
        result.append([])
        for j in range(length):
            a = count
            count += 1
            result[-1].append(a)
    return result


Print(correlation(rand(11)))
