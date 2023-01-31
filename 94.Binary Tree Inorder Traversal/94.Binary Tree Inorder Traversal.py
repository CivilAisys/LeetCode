# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#解法1  中序遍歷  遞回  中序遍歷遍歷直到沒有左子節點時遍將當前加入
def inorderTraversal(root: TreeNode) -> list[int]:
    #結果集
    result = []
    #中序遞迴
    def inorder(node : TreeNode):
        if not node:
            return
        #若還有左子節點 則繼續遍歷
        if node.left:
            inorder(node.left)
        result.append(node.val)
        if node.right:
            inorder(node.right)

    inorder(root)
    return result



#解法2  中序遍歷 左->根->右  使用loop 符合題目 
def inorderTraversal1(root: TreeNode) -> list[int]:
    #結果集
    result = []
    #stack 用於存放需要遍歷的節點 pointer指向節點
    stack = []
    pointer = root
    while pointer or stack:
        #遍歷所有左子節點直到沒有子節點為止
        while pointer:
            stack.append(pointer)
            pointer = pointer.left
        #沒有子節點就將stack內存的節點加入並尋找右節點
        pointer = stack.pop()
        result.append(pointer.val)
        pointer = pointer.right

    return result
