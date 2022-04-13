import matplotlib.pyplot as plt
import yfinance as yf
import random
import math
import matplotlib.pyplot as plt


def generate(n):
    res = []
    for i in range(n):
        res.append(random.randint(100, 110))
    return res


def destroy(arr, n):
    g = {}
    for i in range(n):
        while True:
            k = random.randint(0, len(arr) - 1)
            if arr[k] is not None:
                break
        g[k] = arr[k]
        arr[k] = None
    return [arr, g]


def vinz(array):
    j = {}
    for index in range(len(array)):
        if array[index] is None:
            dop_index = 0
            while array[index] is None:
                if index - dop_index > 0 and array[index - dop_index] is not None:
                    array[index] = array[index - dop_index]
                    j[index] = array[index - dop_index]
                if index + dop_index < len(array) and array[index + dop_index] is not None:
                    array[index] = array[index + dop_index]
                    j[index] = array[index + dop_index]
                dop_index += 1
    return [array, j]


def smoothing(arr, k):
    res = []
    m = []
    for i in range(len(arr)):
        if i == 0:
            res.append(arr[i])
        else:
            window = arr[:i + 1]
            # while math.fabs(window[-1] - (sum(window) / len(window))) / window[-1] > k:
            #     window.pop(0)
            f = False
            while math.fabs((arr[i] - (sum(window) / len(window))) / arr[i]) > k:
                f = True
                # print((sum(window) / len(window)) / arr[i])
                if len(window) > 1:
                    window.pop(0)
                else:
                    break
            if f:
                m.append(len(window))
            res.append(sum(window) / len(window))
    return [res, m]


data = yf.download("YNDX.ME", "2000-09-09", "2022-03-09")
data = data["Adj Close"].to_dict()
data2 = {}
for time in data.keys():
    data2[str(time)[:10]] = float(data[time])


def skolzyashee_srednee(arr, n):
    answer = []
    dates = []
    for i in range(n):
        answer.append(arr[i])
        dates.append(i)
    for i in range(0, len(arr) - n, n):
        a = 0
        for j in range(n):
            a += arr[i + j] * (n + 1 - j)
        a = a * 2 / (n * (n + 1))
        answer.append(a)
        dates.append(i)
    return [answer, dates]


h = []
l = []

a = destroy(generate(10), 3)
b = vinz(a[0])
array = b[0]
x1 = list(b[1].keys())
y1 = list(b[1].values())
x = list(a[1].keys())
y = list(a[1].values())
plt.plot(array)
ar = smoothing(array, 0)
print(max(ar[1]))
plt.plot(ar[0])
plt.scatter(x, y, c="r")
plt.scatter(x1, y1, c="g")
plt.show()

# data_sr = skolzyashee_srednee(list(data2.values()), 20)[0]
# l = skolzyashee_srednee(list(data2.values()), 20)[1]
# for k in range(len(data2.values())):
#     h.append(k)
# plt.plot(l, data_sr)
# plt.plot(h, list(data2.values()))
# plt.show()
