# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
#解法1  遞歸求解兩樹各節點值是否相同
def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    #終止條件  傳入兩個都為None 回傳True or 比對兩者是否一致
    if not p and not q:
        return True    
    if (not p and q) or (not q and p) or (p.val != q.val):
        return False
    
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

