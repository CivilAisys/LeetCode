# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
#解法1  用遞迴2分查找  中間點及為每次上方的節點
def sortedArrayToBST(nums: list[int]) -> TreeNode:
    return helper_function(nums,0, len(nums)-1)


def helper_function(nums: list[int], left: int, right: int) -> TreeNode:
    # 中止條件
    if left > right:
        return None
    mid = left + (right - left) // 2
    cur = TreeNode(nums[mid])
    cur.left = helper_function(nums, left, mid - 1)
    cur.right = helper_function(nums, mid+1, right)
    return cur


