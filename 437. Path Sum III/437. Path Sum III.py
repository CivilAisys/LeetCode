# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 使用遞迴 並在每個節點計算從根節點到當前節點的路徑和
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        def dfs(node, currentSum):
            if not node:
                return 0  # 遞迴終止條件  節點為空 返回0

            count = 0
            currentSum += node.val  # 更新當前路徑和
            if currentSum == targetSum:
                count += 1  # 如果當前路徑和等於目標和，則符合條件的路徑數量加 1

            count += dfs(node.left, currentSum)  # 遞迴計算左子樹符合條件數量
            count += dfs(node.right, currentSum)  # 遞迴計算右子樹

            return count

        # 無根節點直接返回
        if not root:
            return 0

        path_count = dfs(root, 0)  # 遞歸計算從根節點開始的符合條件的路徑數量
        path_count += self.pathSum(root.left, targetSum)  # 遞歸計算左子樹中符合條件的路徑數量
        path_count += self.pathSum(root.right, targetSum)  # 遞歸計算右子樹中符合條件的路徑數量

        return path_count  # 返回最終的路徑數量
