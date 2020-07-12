import ipt
from algorithm.datastruct import ListNode, createlink, traverse


def bubblesort_a(arr):
    l = len(arr)
    i = 0
    while i < l-1:
        j = 0
        flag = True
        while j < l-1-i:
            if arr[j] > arr[j+1]:
                flag = False
                arr[j], arr[j+1] = arr[j+1], arr[j]
            j += 1
        if flag:
            break
        i += 1


def bubblesort_l(head):
    if head is None or head.next is None:
        return head
    pend = None
    while pend is not head.next:
        p = head
        flag = False
        while p.next is not pend:
            if p.val > p.next.val:
                p.val, p.next.val = p.next.val, p.val
                flag = True
            p = p.next
        if flag:
            break
        pend = p
    return head


if __name__ == '__main__':
    arr = [3, 1, 5, 10, 2, 8, 6]
    # bubblesort_a(arr)
    # print(arr)
    head = createlink(arr)
    head = bubblesort_l(head)
    traverse(head)