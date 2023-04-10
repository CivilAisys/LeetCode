# 解法1  使用backTracking進行窮舉  將所有可能組合列出
def permute(nums: list[int]) -> list[list[int]]:
    # 所有結果集
    result = []
    permuteDFS(nums, len(nums), [], result)
    return result

# nums為可選擇的數值 numsLength為最外層初始nums的長度 path為當前決策 滿足條件後加入至totalResult
def permuteDFS(nums: list[int], numsLength: int, path: list[int], totalResult: list[list[int]]):
    # 終止條件 當numsLength == len(path)
    if numsLength == len(path):
        totalResult.append(path)
        return

    for index in range(len(nums)):
        # numsCopy代表剩餘可選擇的數值
        numsCopy = nums.copy()
        numsCopy.pop(index)
        permuteDFS(numsCopy, numsLength, path + [nums[index]], totalResult)
