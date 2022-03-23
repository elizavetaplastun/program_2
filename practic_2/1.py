import random

arr = []
n = random.randint(300, 500)
for i in range(n):
    arr.append(random.randint(1, 50))
arr.sort()
indexes = [i for i in range(n)]
for i in range(10):
    index = random.choice(indexes)
    arr[index] = random.randint(20001, 50000)
print(arr)


def sigma(arr):
    summ = sum(arr)
    n = len(arr)
    medium = summ // n
    s = 0
    for i in arr:
        s += (i - medium) ** 2
    s = (s / (n - 1)) ** 0.5
    return s * 3


def vinzorir(arr):
    sss = sigma(arr)
    for i in range(len(arr)):
        if arr[i] > sss:
            if i == 0:
                arr[i] = random.choice([arr[i + 2], arr[i + 1]])
            elif i == len(arr) - 1:
                arr[i] = random.choice([arr[i - 2], arr[i - 1]])
            else:
                arr[i] = random.choice([arr[i - 1], arr[i + 1]])
    return arr


print(vinzorir(arr[:]))
