import ipt
from algorithm.datastruct import TreeNode, Tree

# 二叉树的递归遍历太过简单，省略


def pretty_print_tree(node, prefix="", isLeft=True):
    if not node:
        print("Empty Tree")
        return

    if node.right:
        pretty_print_tree(node.right, prefix + ("│   " if isLeft else "    "),
                          False)

    print(prefix + ("└── " if isLeft else "┌── ") + str(node.val))

    if node.left:
        pretty_print_tree(node.left, prefix + ("    " if isLeft else "│   "),
                          True)

def pre_order(root):
    st = []
    res = []
    p = root
    while p or st:
        while p:
            res.append(p.val)
            st.append(p)
            p = p.left
        if st:
            p = st.pop(-1)
            p = p.right
            
    return res


def in_order(root):
    st = []
    res = []
    p = root
    while p or st:
        while p:
            st.append(p)
            p = p.left

        if st:
            p = st.pop()
            res.append(p.val)
            p = p.right
    return res


# 使用访问次数标识，来说明某个节点是否为第二次访问，第二次访问时可进行遍历该节点
def post_order1(root):
    st = []
    p = root
    res = []

    while p or st:
        while p:
            st.append(p)
            p.visited = True
            p = p.left
        if st:
            p = st.pop()
            if p.visited:
                p.visited = False
                st.append(p)
                p = p.right
            else:
                res.append(p.val)
                p = None
    return res


# 要保证根结点在左孩子和右孩子访问之后才能访问，因此对于任一结点P，先将其入栈。
# 如果P不存在左孩子和右孩子，则可以直接访问它；
# 或者P存在左孩子或者右孩子，但是其左孩子和右孩子都已被访问过了，则同样可以直接访问该结点。
# 若非上述两种情况，则将P的右孩子和左孩子依次入栈，这样就保证了每次取栈顶元素的时候，
# 左孩子在右孩子前面被访问，左孩子和右孩子都在根结点前面被访问。
def post_order2(root):
    if root is None:
        return []
    res = []
    st = [root]
    pre = None
    while st:
        cur = st[-1]
        if (cur.left is None and cur.right is None) or (
            pre is not None and (pre == cur.left or pre == cur.right)):
            cur = st.pop()
            res.append(cur.val)
            pre = cur
        else:
            if cur.right:
                st.append(cur.right)
            if cur.left:
                st.append(cur.left)
    return res
            

if __name__ == '__main__':
    btree = Tree([4, 3, 2, None, 6, 7, None, 8])
    pretty_print_tree(btree.root)
    # res = pre_order(btree.root)
    # res = in_order(btree.root)
    res = post_order2(btree.root)
    print(res)
