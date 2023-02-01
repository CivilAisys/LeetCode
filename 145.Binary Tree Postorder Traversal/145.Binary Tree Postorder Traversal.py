# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# 解法1  模板方法  同94.144  後序遍歷  左 -> 右 -> 根  往左下  直到沒有右子節點
# 將先序遍歷的根-左-右順序變為根-右-左，再翻轉變為後序遍歷的左-右-根，翻轉還是改變結果 res 的加入順序，
# 然後把更新輔助結點p的左右順序換一下即可
def postorderTraversal(root: TreeNode) -> list[int]:
    # 結果集
    result = []
    # 輔助的stack及節點p
    stack = []
    p = root

    while stack or p:
        if p:
            stack.append(p)
            result.insert(0, p)
            p = p.right
        else:
            p = stack.pop()
            p = p.left
    return result
