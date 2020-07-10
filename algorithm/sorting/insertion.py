

def insertionsort_a(arr):
    l = len(arr)
    for i in range(1, l):
        cur = arr[i]
        idx = i-1
        while idx >= 0 and arr[idx] > cur:
            arr[idx+1] = arr[idx]
            idx -= 1
        arr[idx+1] = cur


if __name__ == '__main__':
    arr = [3, 1, 5, 10, 2, 8, 6]
    insertionsort_a(arr)
    print(arr)
        
        