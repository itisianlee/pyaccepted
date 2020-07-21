import ipt
from algorithm.datastruct import TreeNode, Tree


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


if __name__ == '__main__':
    btree = Tree([4, 3, 2, None, 6, None, 8])
    res = pre_order(btree.root)
    print(res)
