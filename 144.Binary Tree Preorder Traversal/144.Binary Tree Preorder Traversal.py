# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# 解法1  前序遍歷  遍歷須為根-左-右  使用一個stack輔助確認是否還有節點需要遍歷
# 前序是直到沒有左子節點 才會找右子節點  與中序遍歷一樣
# 只是前序會在過程中就將遍力道的節點加入結果中序不會
def preorderTraversal(root: TreeNode) -> list[int]:
    if not root:
        return []
    # 結果集 and  stack輔助(先將root放入)
    result = []
    stack = [root]
    # loop condition is stack not empty
    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return result


# 解法2  同94題解法三  前序遍歷  根 -> 左 -> 右  往左下 直到沒有左子節點 過程中的都要加入
# 輔助結點p初始化為根結點，while 循環的條件是棧不為空或者輔助結點p不為空，
# 在迴圈中首先判斷如果輔助結點p存在，那麼先將p加入棧中，然後將p的結點值加入結果 res 中，此時p指向其左子結點。
# 否則如果p不存在的話，表明沒有左子結點，取出棧頂結點，將p指向棧頂結點的右子結點
def preorderTraversal(root: TreeNode) -> list[int]:
    #結果集
    result = []
    #輔助的stack及節點p
    stack = []
    p = root

    while stack or p:
        if p:
            stack.append(p)
            result.append(p.val)
            p = p.left
        else:
            p = stack.pop()
            p = p.right
    return result
