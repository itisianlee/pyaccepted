def selectionsort(arr):
    l = len(arr)
    for i in range(l):
        minidx = i
        for j in range(i, l):
            if arr[j] < arr[minidx]:
                minidx = j
        arr[i], arr[minidx] = arr[minidx], arr[i]


if __name__ == '__main__':
    arr = [3, 1, 5, 10, 2, 8, 6]
    selectionsort(arr)

        