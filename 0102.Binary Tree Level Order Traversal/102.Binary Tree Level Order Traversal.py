import collections
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# 解法1  BFS  樹的層序遍歷
# 建立deque輔助
def levelOrder(root: TreeNode) -> list[list[int]]:
    # 沒有節點  直接回傳空陣列
    if not root:
        return []
    # 遍歷的結果(二維陣列)
    result = []
    # 輔助的deque
    deque = collections.deque()
    deque.append(root)

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
        result.append(one_level)

    return result
