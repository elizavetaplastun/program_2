arr = list(map(int, input().split()))


def buble_sort(arr):
    N = len(arr)
    for i in range(N - 1):
        for j in range(N - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def gnome_sort(arr):
    N = len(arr)
    i = 1
    while i < N:
        if (arr[i - 1] <= arr[i]):
            i += 1
        else:
            tmp = arr[i]
            arr[i] = arr[i - 1]
            arr[i - 1] = tmp
            i -= 1
            if (i == 0):
                i = 1
    return arr


def bucket_sort(arr):
    max_value = max(arr)
    N = max_value / len(arr)

    buckets_list = []
    for x in range(len(arr)):
        buckets_list.append([])

    for i in range(len(arr)):
        j = int(arr[i] / N)
        if j != len(arr):
            buckets_list[j].append(arr[i])
        else:
            buckets_list[len(arr) - 1].append(arr[i])

    for k in range(len(arr)):
        buble_sort(buckets_list[k])

    sorted_arr = []
    for x in range(len(arr)):
        sorted_arr = sorted_arr + buckets_list[x]
    return sorted_arr


def heapify(arr, len, index):
    largest = index
    left = (2 * index) + 1
    right = (2 * index) + 2

    if left < len and arr[left] > arr[largest]:
        largest = left

    if right < len and arr[right] > arr[largest]:
        largest = right

    if largest != index:
        arr[index], arr[largest] = arr[largest], arr[index]
        heapify(arr, len, largest)


def heap_sort(arr):
    n = len(arr)

    for i in range(n, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr


print(buble_sort(arr[:]))
print(gnome_sort(arr[:]))
print(buble_sort(arr[:]))
print(heap_sort(arr[:]))
