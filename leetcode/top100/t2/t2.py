def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    carry = 0
    p = l1
    q = l2
    r = ListNode()
    r.next = p
    while p and q:
        cur = p.val + q.val + carry
        carry = cur // 10
        cur %= 10
        p.val = cur
        p = p.next
        q = q.next
        r = r.next
        
    while p:
        cur = p.val + carry
        carry = cur // 10
        cur %= 10
        p.val = cur
        p = p.next
        r = r.next
    
    while q:
        cur = q.val + carry
        carry = cur // 10
        cur %= 10
        q.val = cur
        r.next = q
        q = q.next
        r = r.next
        
    if carry:
        r.next = ListNode(carry)
    return l1