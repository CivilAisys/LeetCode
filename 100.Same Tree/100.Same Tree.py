# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
#解法1  遞歸求解兩樹各節點值是否相同
def isSameTree(p: TreeNode, q: TreeNode) -> bool:


    


    return False

#解法2 while loop 使用兩個quene輔助比對
def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    quene_p = [p]
    quene_q = [q]
    while quene_p and quene_q:
        if quene_p.pop() != 


    return True