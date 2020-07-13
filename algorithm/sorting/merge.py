import ipt
from algorithm.datastruct import ListNode, createlink, traverse


def mergesort_a(arr):
    l = len(arr)
    def merge(arr, left, mid, right):
        i = left
        j = mid + 1
        tmp = []
        while i <= mid and j <= right:
            if arr[i] < arr[j]:
                tmp.append(arr[i])
                i += 1
            else:
                tmp.append(arr[j])
                j += 1
        while i <= mid:
            tmp.append(arr[i])
            i += 1
        while j <= right:
            tmp.append(arr[j])
            j += 1

        for x in tmp:
            arr[left] = x
            left += 1

    def sort(arr, left, right):
        if left < right:
            mid = (left + right) // 2
            sort(arr, left, mid)
            sort(arr, mid+1, right)
            merge(arr, left, mid, right)
    sort(arr, 0, l-1)


def merge(h1, h2):
    if h1 is None:
        return h2
    if h2 is None:
        return h1
    if h1.val < h2.val:
        head = h1
        h1 = h1.next
    else:
        head = h2
        h2 = h2.next
    p = head
    while h1 and h2:
        if h1.val < h2.val:
            p.next = h1
            h1 = h1.next
        else:
            p.next = h2
            h2 = h2.next
        p = p.next
    p.next = h1 if h1 else h2
    return head


def mergesort_l(head):
    if head is None or head.next is None:
        return head
    fast = head
    slow = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    fast = slow.next
    slow.next = None

    head = mergesort_l(head)
    fast = mergesort_l(fast)
    return merge(head, fast)


if __name__ == '__main__':
    arr = [3, 1, 5, 10, 2, 8, 6]
    # mergesort_a(arr)
    # print(arr)
    head = createlink(arr)
    head = mergesort_l(head)
    traverse(head)
        