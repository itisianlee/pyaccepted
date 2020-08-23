def binary_search(arr, value):
    n = len(arr)
    low = 0
    high = n-1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == value:
            return mid
        elif arr[mid] < value:
            low = mid + 1
        else:
            high = mid - 1 

    return -1