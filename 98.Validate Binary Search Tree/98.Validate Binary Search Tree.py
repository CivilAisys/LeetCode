# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# 解法1 使用DFS並利用BST的特性 將最大最小值最為區間來做比對
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return helper_function(root, float('-inf'), float('inf'))

# DFS 條件為區間
def helper_function(node: TreeNode, low , high) -> bool:
    # 中止條件
    if not node:
        return True
    # 超過區間
    if node.val <= low or node.val >= high:
        return False

    return helper_function(node.left, low, node.val) and helper_function(node.right, node.val, high)
