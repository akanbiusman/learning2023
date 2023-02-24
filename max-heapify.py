def max_heapify(arr, i):
    l = left(i)
    r = right(i)

    if l < len(arr) and arr[l] > arr[i]:
        largest = l
    else:
        largest = i

    if r < len(arr) and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        max_heapify(arr, largest)


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def build_heap(arr):
    n = (len(arr) // 2) - 1
    for i in range(n, -1, -1):
        max_heapify(arr, i)


arr = [50, 30, 20, 15, 10, 8, 24, 60]
print(build_heap(arr))
