from datastruct import ListNode, createlink, traverse

def selectionsort_a(arr):
    l = len(arr)
    for i in range(l):
        minidx = i
        for j in range(i, l):
            if arr[j] < arr[minidx]:
                minidx = j
        arr[i], arr[minidx] = arr[minidx], arr[i]


def selectionsort_l1(head):
    p = head
    while p:
        q = p
        minnode = q
        while q:
            if q.val < minnode.val:
                minnode = q
            q = q.next
        p.val, minnode.val = minnode.val, p.val
        p = p.next


if __name__ == '__main__':
    arr = [3, 1, 5, 10, 2, 8, 6]
    # selectionsort_a(arr)
    head = createlink(arr)
    selectionsort_l1(head)
    traverse(head)

        