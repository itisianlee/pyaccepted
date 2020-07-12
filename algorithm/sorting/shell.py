def shellsort(arr):
    l = len(arr)
    gap = l // 2

    while gap > 0:
        for i in range(gap, l):
            j = i
            cur = arr[i]
            while j-gap >= 0 and cur < arr[j-gap]:
                arr[j] = arr[j-gap] 
                j = j - gap
            arr[j] = cur
        gap = gap // 2


if __name__ == '__main__':
    arr = [3, 1, 5, 10, 2, 8, 6]
    shellsort(arr)
    print(arr)