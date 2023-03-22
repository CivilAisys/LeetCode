# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# 解法1 暴力解 dfs  找出所有元素並加入至陣列中進行排序 回傳list[k-1]
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        arr = []

        def dfs(node: TreeNode) -> None:
            # 中止條件
            if not node:
                return
            arr.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        arr.sort()
        return arr[k-1]


# 解法2 中序遍歷  並使用計數器計算當前順序  當順序 = k時回傳
class Solution1:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        arr = []
        self.inorder(root, arr)
        return arr[k-1]
    # 使用中序遍歷會依照大小遍歷的特性  回傳遍歷到的第k個值即可

    def inorder(self, node: TreeNode, arr: list) -> None:
        if not node:
            return
        # 若還有左子節點 則繼續遍歷
        if node.left:
            self.inorder(node.left, arr)
        arr.append(node.val)
        if node.right:
            self.inorder(node.right, arr)
