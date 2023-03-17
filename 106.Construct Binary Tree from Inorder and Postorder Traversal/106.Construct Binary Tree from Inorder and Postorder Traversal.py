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
                   pright: int) -> TreeNode:
        if ileft > iright or pleft > pright:
            return None
        # 後序的尾為根結點或葉節點  找出在中序中(根)節點的位置i
        cur = TreeNode(postorder[pright])
        i = 0
        for j in range(ileft, len(inorder)):
            if inorder[j] == cur.val:
                i = j
                break
        # 依照每個找到的節點分為左右兩邊進行遞規調用
        # i-ileft是計算inorder中根節點位置和左邊起始點的距離
        # 中序找到節點處  代表節點左側為左子樹  節點右側為右子樹
        cur.left = self.build_tree(
            inorder, ileft, i-1, postorder, pleft, pleft+i-ileft-1)
        # 後序的pright相對於中序切分出的右子樹偏移量為1 故pright = pright -1 且pright - 1 皆為右子樹的葉節點
        cur.right = self.build_tree(
            inorder, i + 1, iright, postorder, pleft + i - ileft, pright - 1)

        return cur

test = Solution()
test.buildTree([11,4,5,13,8,9],[11,4,13,9,8,5])