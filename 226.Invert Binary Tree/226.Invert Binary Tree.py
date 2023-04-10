class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
# 解法1  遞迴將左右節點調換
def invertTree(root: TreeNode) -> TreeNode:
    if not root:
        return None
    # 若還有左右節點  繼續進行遞迴調換 temp保存左節點  以免變更被後被丟入錯誤的右節點
    temp = root.left
    root.left = invertTree(root.right)
    root.right = invertTree(temp)

    # 回傳自己
    return root


# 解法2  使用quene進行輔助  若根節點有值則加入quene中進行左右調換 若左右節點有值 則再加入quene中
def invertTree(root: TreeNode) -> TreeNode:
    # 輔助用的quene
    quene = []
    if root:
        quene.append(root)
    # 若quene內還有值
    while quene:
        cur_node = quene.pop()
        temp = cur_node.left
        # 節點左右調換
        cur_node.left = cur_node.right
        cur_node.right = temp

        # 若左右節點還有值  加入quene
        if cur_node.left:
            quene.append(cur_node.left)
        if cur_node.right:
            quene.append(cur_node.right)

    # 最後回傳root即可
    return root
