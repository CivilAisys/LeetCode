# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 解法1
# 如果當前結點不等於p或q，p和q要麼分別位於左右子樹中，要麼同時位於左子樹，或者同時位於右子樹：

# 若p和q分別位於左右子樹中，那麼對左右子結點調用遞歸函數，會分別返回p和q結點的位置，
# 而當前結點正好就是p和q的最小共同父結點，直接返回當前結點即可，這就是題目中的例子1的情況。

# 若p和q同時位於左子樹，這裡有兩種情況，一種情況是 left 會返回p和q中較高的那個位置，
# 而 right 會返回空，所以最終返回非空的 left 即可，這就是題目中的例子2的情況。還有一種情況是會返回p和q的最小父結點，就是說當前結點的左子樹中的某個結點才是p和q的最小父結點，會被返回。

# 若p和q同時位於右子樹，同樣這裡有兩種情況，一種情況是 right 會返回p和q中較高的那個位置，
# 而 left 會返回空，所以最終返回非空的 right 即可，還有一種情況是會返回p和q的最小父結點，就是說當前結點的右子樹中的某個結點才是p和q的最小父結點
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or p.val == root.val or q.val == root.val:
            return root
        # 若只有left代表p.q都在左子樹  誰先被找到就先回傳誰  即為LCS
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        # 若左右都有  代表當前為LCS
        if left and right:
            return root
        return left if left else right
