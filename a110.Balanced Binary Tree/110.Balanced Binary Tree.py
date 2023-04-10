class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 解法1 高度平衡二叉樹是每一個結點的兩個子樹的深度差不能超過1
# 計算每個節點的深度
# 我們發現子樹不平衡，則不計算具體的深度，而是直接返回-1。
# 那麼優化后的方法為：對於每一個節點，我們通過checkDepth方法遞歸獲得左右子樹的深度，如果子樹是平衡的，則返回真實的深度，若不平衡，直接返回-1，此方法時間複雜度O（N），空間複雜度O（H）
def isBalanced(root: TreeNode) -> bool:
    if checkDepth(root) == -1:
        return False 
    return True

#計算深度  若不平衡  直接返回-1
def checkDepth(root: TreeNode) -> int:
    if not root:
        return 0

    left = checkDepth(root.left)
    if left == -1:
        return -1
    right = checkDepth(root.right)
    if right == -1:
        return -1
    #左右子樹差異
    diff = abs(left -right)
    if diff > 1:
        return -1
    else:
        return 1 + max(left,right)


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(2)
d = TreeNode(3)
e = TreeNode(3)
f = TreeNode(4)
g = TreeNode(4)


a.left = b
a.right = c
b.left = d
b.right = e
d.left = f
d.right = g

isBalanced(a)

