# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 解法1
# 後序的順序最後一個是根，故可得根結點，並可以其在中序中找到根結點，並對其左右調用遞規函式
class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode:
        return self.build_tree(inorder, 0, len(inorder) - 1, postorder, 0, len(postorder) - 1)

    def build_tree(self, inorder: list[int], ileft: int, iright: int, postorder: list[int], pleft: int,
                   pright: int) -> None:

        if ileft > iright or pleft > pright:
            return None
        # 後序的尾為根結點
        cur = TreeNode(postorder[pright])
        
