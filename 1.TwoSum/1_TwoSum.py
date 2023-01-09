# 解法1
def twoSum(nums: list[int], target: int) -> list[int]:
    # 要回傳的結果陣列
    result = []

    # 巢狀迴圈加總與target比對
    for index in range(0, len(nums)):

        # 內部迴圈要跳過上層已遍歷過的index
        for index1 in range(index+1, len(nums)):
            if (nums[index] + nums[index1]) == target:
                result.append(index)
                result.append(index1)

    return result

# 解法2


def twoSum1(nums: list[int], target: int) -> list[int]:
    # 使用dic  key儲存nums[i]的值 value儲存index
    map = {}
    for index in range(len(nums)):
        # target - 當前元素
        minus = target - nums[index]

        # 相減完結果在map內即回傳
        if minus in map:
            return [map[minus], index]
        else:
            map[nums[index]] = index
