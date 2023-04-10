# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# 解法1 backtracing 窮舉 DFS
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> list[list[int]]:
        result = []  # 結果集
        self.helper_function(root, targetSum, [], result)
        return result
    # path為當前累積走的路徑 result為所有符合的結果集

    def helper_function(self, node: TreeNode, targetSum: int, path: list[int], result: list[list[int]]):
        # 中止條件 1. node沒有值 
        if not node:
            return
        path.append(node.val)
        # 成功條件 值相等 且沒有左右子節點  則該節點為葉節點
        if not node.left and not node.right and sum(path) == targetSum:
            result.append(path[:])

        # 向左右進行DFS查找
        self.helper_function(node.left, targetSum, path, result)
        self.helper_function(node.right, targetSum, path, result)
        path.pop()  # 避免前面使用path.copy()占用記憶體空間
