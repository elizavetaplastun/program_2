import matplotlib.pyplot as plt


def approx(x, y):
    n = len(x)
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


x = [2.068185862,
     2.005180513,
     1.977723605,
     1.960946196,
     1.951337519,
     1.934498451,
     1.921166051]
y = [-0.5245003308,
     -0.3490986704,
     -0.2251261091,
     -0.1294595885,
     -0.05180010856,
     0.01334546499,
     0.06925534552]
a, b = approx(x, y)

print(a, b)
