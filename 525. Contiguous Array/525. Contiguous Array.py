# 解法1
# 我們可以用一個 count 變量來計算當前位置 i 的 1 和 0 的差值，即 count += 1 if nums[i] == 1 else -1。
# 然後，我們使用哈希表來存儲每個差值第一次出現的位置。如果在以前的位置中我們已經見過相同的差值，
# 那麼當前位置與之前的相同差值的位置之間的子陣列必定是具有相等數量的 0 和 1 的連續子陣列。
# 這樣，我們可以計算這樣的子陣列的長度，並用當前找到的最長子陣列長度來更新答案。
class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        count = 0  # 計算差值
        result = 0  # 　結果
        # 紀錄每個差值出現的位置 且須初始化差值0在-1處
        # 若只有[0,1] 時 長度為2 差值0第二次出現位置為1
        dic = {0: -1}

        # 遍歷數組
        for i in range(len(nums)):
            count += (1 if nums[i] == 1 else -1)  # 計算差值
            if count in dic:
                # 當前差值位置與前一次差值出現位置中間勢必有想同數量的0跟1
                result = max(result, i - dic[count])
            else:
                dic[count] = i  # 更新該差值出現位置
        return result
