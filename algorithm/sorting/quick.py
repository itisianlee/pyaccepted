import ipt
from algorithm.datastruct import ListNode, createlink, traverse


def quicksort_a(arr):
    l = len(arr)
    def quicksort(arr, left, right):
        if left <= right:
            idx = partition(arr, left, right)
            quicksort(arr, left, idx-1)
            quicksort(arr, idx+1, right)

    def partition(arr, left, right):
        pivot = left
        idx = pivot + 1

        for i in range(idx, right+1):
            if arr[i] < arr[pivot]:
                arr[i], arr[idx] = arr[idx], arr[i]
                idx += 1

        arr[idx-1], arr[left] = arr[left], arr[idx-1]
        return idx-1

    quicksort(arr, 0, l-1)


def quicksort_l_switch_val(head):
    if head is None or head.next is None:
        return head
    def partition(left, right):
        pivot = left.val
        p = left.next
        q = left
        while p is not right:
            if p.val < pivot:
                p.val, q.next.val = q.next.val, p.val
                q = q.next
            p = p.next
        left.val, q.val = q.val, left.val
        return q

    def sort(head, tail):
        if head is not tail and head.next is not tail:
            q = partition(head, tail)
            sort(head, q)
            sort(q.next, tail)
    sort(head, None)
    return head


def quicksort_l_switch_node(head):
    if head is None or head.next is None:
        return head

    def partition(pre, left, right):
        pivot = left.val
        h1 = ListNode(0)
        h2 = ListNode(0)
        big = h1
        sma = h2
        p = left.next
        while p is not right:
            if p.val < pivot:
                sma.next = p
                sma = p
            else:
                big.next = p
                big = p
            p = p.next
        big.next = right
        sma.next = left
        left.next = h1.next
        pre.next = h2.next
        return left

    def sort(pre, head, tail):
        if head is not tail and head.next is not tail:
            q = partition(pre, head, tail)
            sort(pre, pre.next, q)
            sort(q, q.next, tail)

    headpre = ListNode(0)
    headpre.next = head
    sort(headpre, head, None)
    return headpre.next
    

if __name__ == '__main__':
    # arr = [3, 1, 5, 10, 2, 8, 6]
    arr = [3, 2, 1]
    # quicksort_a(arr)
    # print(arr)
    head = createlink(arr)
    # quicksort_l_switch_val(head)
    head = quicksort_l_switch_node(head)
    traverse(head)

