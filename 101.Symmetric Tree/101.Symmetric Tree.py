# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# 解法1  遞迴比對兩節點的左是否等於右(對稱)
def isSymmetric(root: TreeNode) -> bool:
    return helper_function(root.left, root.right)


def helper_function(left: TreeNode, right: TreeNode) -> None:
    # 中止條件
    # 左 右都沒有 回傳True
    if not left and not right:
        return True
    # 短路運算 符合其中一個條件就回傳False
    elif (not left and right) or (not right and left) or (left.val != right.val) or (right.val != left.val):
        return False

    return helper_function(left.left, right.right) and helper_function(left.right, right.left)


# 解法2 題目額外要求使用迭代進行比對
def isSymmetric1(root: TreeNode) -> bool:
    # 使用兩個quene進行左右兩兩比對 q1放左子樹的左右節點 q2放右子樹的左右節點
    q1, q2 = [], []
    q1.append(root.left)
    q2.append(root.right)

    while q1 and q2:
        left = q1.pop()
        right = q2.pop()
        #開始比對
        #左右都沒有 繼續迴圈 
        if not left and  not right:
            continue
        #左或右沒有
        if (not left and right) or (not right and left):
            return False
        #左右值不一致
        if left.val != right.val:
            return False
        q1.append(left.left)
        q1.append(left.right)
        q2.append(right.right)
        q2.append(right.left)

    return True
