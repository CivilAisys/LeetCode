# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 解法1 同102層歷的變形 只保留每一層最右邊的的數位即可
class Solution:
    def rightSideView(self, root: TreeNode) -> list[int]:
        # 沒有結點  回傳空陣列
        if not root:
            return []
        # 結果集
        result = []
        # 輔助用的deque 並將跟節點放入
        deque = collections.deque()
        deque.append(root)

        # 只要deque內還有值便繼續遍歷
        while deque:
            # 每層的一維陣列
            one_level = []
            # 遍歷上層的節點(deque)  將節點加入至one_level並將遍歷到的節點左右加入至deque內
            for i in range(len(deque)):
                node = deque.popleft()
                one_level.append(node.val)
                if node.left:
                    deque.append(node.left)
                if node.right:
                    deque.append(node.right)
            # 只加入每層最右邊的節點
            result.append(one_level[-1])

        return result
