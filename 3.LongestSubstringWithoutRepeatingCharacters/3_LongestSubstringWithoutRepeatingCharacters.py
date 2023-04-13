# 解法1
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 傳入空字串的情形
        if len(s) == 0:
            return 0

        # 存放每一個字元最後出現的索引
        dic = {}
        # 不重複字串的開頭索引
        left = 0
        # 最大長度至少為1
        maxLength = 1

        for index in range(len(s)):
            # 若當前字元最後出現索引 大於等於不重複開頭  更新開頭索引
            # 當前字元不在dic內  不執行if判斷
            if s[index] in dic:
                if dic[s[index]] >= left:
                    left = dic[s[index]] + 1

            # 紀錄每個字元最新索引
            dic[s[index]] = index
            # 更新最大長度
            maxLength = max(maxLength, index - left + 1)

        return maxLength

test = Solution()
print(test.lengthOfLongestSubstring("abcabcbb"))
