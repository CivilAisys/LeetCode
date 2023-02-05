# 解法1 因題目說對每個數做平方再存入新陣列排序是簡單不重要的 故需要用其他時間為O(n)的方法做
# 使用雙指標對頭尾  頭尾比較絕對值 每次把大的塞入對應位置即可
def sortedSquares(nums: list[int]) -> list[int]:
    # 結果陣列 要先產出與nums長度一致的陣列
    length = len(nums)
    result = [0 for _ in range(length)]
    # 頭尾指針及當前要加入的index位置(預設為尾部)
    left, right, index = 0, length-1, length-1

    # 迴圈比對頭尾絕對值
    while index >= 0:
        # 左大於右
        if abs(nums[left]) > abs(nums[right]):
            result[index] = nums[left] * nums[left]
            left += 1
        else:
            result[index] = nums[right] * nums[right]
            right -= 1
        index -= 1
    
    return result