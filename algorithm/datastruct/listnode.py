class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def createlink(arr=None):
    assert arr
    head = ListNode(arr[0])
    p = head
    for x in arr[1:]:
        tmp = ListNode(x)
        p.next = tmp
        p = p.next
    return head

def traverse(head):
    if head is None:
        return
    p = head
    while p:
        print(p.val, end=' ')
        p = p.next
