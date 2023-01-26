class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 解法1
# 這道題讓我們求二叉樹的直徑，並告訴了我們直徑就是兩點之間的最遠距離，
# 根據題目中的例子也不難理解題意。
# 我們再來仔細觀察例子中的那兩個最長路徑[4，2，1，3] 和 [5，2，1，3]，我們轉換一種角度來看，
# 是不是其實就是根結點1的左右兩個子樹的深度之和呢。那麼我們只要對每一個結點求出其左右子樹深度之和，
# 這個值作為一個候選值，然後再對左右子結點分別調用求直徑對遞歸函數，這三個值相互比較，取最大的值更新結果res，
# 因為直徑不一定會經過根結點，所以才要對左右子結點再分別算一次。
# 為了減少重複計算，我們用哈希表建立每個結點和其深度之間的映射，這樣某個結點的深度之前計算過了，就不用再次計算了


def diameterOfBinaryTree(root: TreeNode) -> int:
    # 結果 因為在遞回含式內更新result 會有global variable的問題  故宣告陣列並保存最大路徑結果
    result = [0]
    #使用cache(dic) 來記錄已經執行過的結果
    cache = {}
    def maxDepth(node: TreeNode) -> int:
        if not node:
            return 0
        #若已經計算過  直接回傳該節點最大深度
        if node.val in cache:
            return cache[node.val]

        # 計算左右子樹最深度 最後回傳深度+1 即為當前節點左or右最大深度
        left = maxDepth(node.left)
        right = maxDepth(node.right)
        # 更新result
        result[0] = max(result[0], left + right)
        cache[id(node)] = max(left, right) + 1
        return cache[id(node)]
        
    maxDepth(root)
    return result[0]

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
a.left = b
a.right = c 
b.left = d 
b.right = e

diameterOfBinaryTree(a)


