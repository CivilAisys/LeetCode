# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# 解法1 同106
# 前序的順序第一個是根，故可得根結點
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        return self.build_tree(preorder, 0, len(preorder)-1, inorder, 0, len(inorder)-1)

    def build_tree(self, preorder: list[int], pleft: int, pright: int, inorder: list[int], ileft: int,
                   iright: int) -> TreeNode:
        if ileft > iright or pleft > pright:
            return None
        # 前序的頭為根結點或葉節點  找出在中序中(根)節點的位置i
        cur = TreeNode(preorder[pleft])
        i = 0
        for j in range(ileft, len(inorder)):
            if inorder[j] == cur.val:
                i = j
                break
        cur.left = self.build_tree(
            preorder, pleft+1, pleft+i-ileft, inorder, ileft, i-1)
        # 前序的pleft相對於中序切分出的右子樹偏移量為1 故pleft = pleft + 1 且pleft + 1 皆為右子樹的葉節點
        cur.right = self.build_tree(
            preorder, pleft+i-ileft+1, pright, inorder, i+1, iright)
        return cur


test = Solution()
test.buildTree([5, 4, 11, 8, 13, 9], [11, 4, 5, 13, 8, 9])
