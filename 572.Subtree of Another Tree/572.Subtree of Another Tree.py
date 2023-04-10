# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# 解法1
# 子樹必須是從葉結點開始的，中間某個部分的不能算是子樹，那麼我們轉換一下思路，
# 是不是從s的某個結點開始，跟t的所有結構都一樣，那麼問題就轉換成了判斷兩棵樹是否相同
# 先從s的根結點開始，跟t比較，如果兩棵樹完全相同，那麼返回true，
# 否則就分別對s的左子結點和右子結點調用遞歸再次來判斷是否相同，只要有一個返回true了，就表示可以找得到
def isSubtree(root: TreeNode, subRoot: TreeNode) -> bool:
    if not root:
        return False
    # 先比較最初跟節點與t是否相同  若不相同  則對根結點的左右再去做比對尋找
    if isSame(root, subRoot):
        return True
    # 左右子樹其中一個完全相同即可
    return isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)
# 判斷傳進的兩個節點是否一致
def isSame(s: TreeNode, t: TreeNode)-> bool:
    # 終止條件
    # 兩個都為None  相同
    if not s and not t:
        return True
    # 一個None 一個不為None 不相同
    if not s or not t:
        return False
    # 值不相同 故不相同
    if s.val != t.val:
        return False
    #上述都過的話  再去比對左右節點是否一致
    return isSame(s.left, t.left) and isSame(s.right, t.right)




a = TreeNode(3)
b = TreeNode(4)
c = TreeNode(5)
d = TreeNode(1)
e = TreeNode(2)
k = TreeNode(0)
a.left = b
a.right = c
b.left = d
b.right = e
e.left = k

f = TreeNode(4)
g = TreeNode(1)
h = TreeNode(2)
f.left = g
f.right = h
print(isSubtree(a, f))

