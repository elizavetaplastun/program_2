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
