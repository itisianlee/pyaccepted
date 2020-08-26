这个题还是笔记容易想到最优解法的，但是实现形式上可以有更好的

下面这个是直觉的做法
```
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
```

实际上可以将其以更简化的形式写出来的
```
def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    carry = 0
    p = l1
    q = l2
    dummyhead = ListNode()
    r = dummyhead
    while p or q:
        x = p.val if p else 0
        y = q.val if q else 0
        cur = x + y + carry
        carry = cur // 10
        cur %= 10
        r.next = ListNode(cur)
        r = r.next
            
        p = p.next if p else None
        q = q.next if q else None
    if carry:
        r.next = ListNode(carry)
    return dummyhead.next
```
这种形式虽然看起来笔记简单，但是包含了太多的判断，花费更多的时间

时间复杂度：O(max(m, n)), 空间复杂度：O(1)（第一种方法）