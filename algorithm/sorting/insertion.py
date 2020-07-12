import ipt
from algorithm.datastruct import ListNode, createlink, traverse


def insertionsort_a(arr):
    l = len(arr)
    for i in range(1, l):
        cur = arr[i]
        idx = i-1
        while idx >= 0 and arr[idx] > cur:
            arr[idx+1] = arr[idx]
            idx -= 1
        arr[idx+1] = cur


def insertionsort_l(head):
    if head is None or head.next is None:
        return head
    # For convenience, add headnode
    pstart = ListNode(-1)
    p = head.next
    pstart.next = head
    pend = head
    while p:
        t = pstart.next
        pre = pstart
        while t is not p and p.val >= t.val:
            t = t.next
            pre = pre.next
        if t is p:
            pend = p
        else:
            pend.next = p.next
            pre.next = p
            p.next = t
        p = pend.next
    head = pstart.next
    del pstart
    return head


if __name__ == '__main__':
    arr = [3, 1, 5, 10, 2, 8, 6]
    # insertionsort_a(arr)
    head = createlink(arr)
    head = insertionsort_l(head)
    traverse(head)
        