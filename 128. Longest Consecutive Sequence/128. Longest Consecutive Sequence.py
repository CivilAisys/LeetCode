# 解法1 
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set =  set(nums) # 使用set去重  並使查找速度變為O(1)
        longest_streak = 0 #初始化最大連續次數
        # 遍歷num_set
        for num in num_set:
            if num - 1 not in num_set: # 確認是否為序列起頭
                current_num = num
                current_streak = 1
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                longest_streak = max(longest_streak,current_streak)
        return longest_streak