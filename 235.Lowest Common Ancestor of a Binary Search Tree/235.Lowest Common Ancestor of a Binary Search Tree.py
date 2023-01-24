class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# 二叉搜索樹的特點是左<根<右，所以根節點的值一直都是中間值，
# 大於左子樹的所有節點值，小於右子樹的所有節點值，
# 那麼我們可以做如下的判斷，如果根節點的值大於p和q之間的較大值，說明p和q都在左子樹中，那麼此時我們就進入根節點的左子節點繼續遞歸，
# 如果根節點小於p和q之間的較小值，說明p和q都在右子樹中，那麼此時我們就進入根節點的右子節點繼續遞歸，
# 如果都不是，則說明當前根節點就是最小共同父節點，直接返回即可
def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    # 終止條件 節點為None
    if not root:
        return None

    if root.val > max(p.val, q.val):
        return lowestCommonAncestor(root.left, p, q)
    elif root.val < min(p.val, q.val):
        return lowestCommonAncestor(root.right, p, q)
    else:
        return root


a = TreeNode(6)
b = TreeNode(2)
c = TreeNode(8)
d = TreeNode(0)
e = TreeNode(4)
f = TreeNode(7)
g = TreeNode(9)
h = TreeNode(3)
i = TreeNode(5)

a.left = b
a.right = c
b.left = d
b.right = e
e.left = h
e.right = i
c.left = f
c.right = g

print(lowestCommonAncestor(a, b, e))


# 解法2 用個 while 循環來代替遞歸調用即可，然後不停的更新當前的根節點
def lowestCommonAncestor1(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    while True:
        if root.val > max(p.val, q.val):
            root = root.left
        elif root.val < min(p.val, q.val):
            root = root.right
        else:
            break
    return root