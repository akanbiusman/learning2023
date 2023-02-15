def mgSort(arr):
    mgSort2(arr, 0, len(arr) - 1)
    return arr


def mgSort2(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        mgSort2(arr, left, mid)
        mgSort2(arr, mid + 1, right)
        merge(arr, left, mid, right)


def merge(arr, left, mid, right):
    L = arr[left:mid + 1]
    R = arr[mid + 1:right + 1]
    L.append(999999999)
    R.append(999999999)
    i = j = 0

    for k in range(left, right + 1):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1


print(mgSort([3, 5, 1, 2, 8, 9, 10]))
