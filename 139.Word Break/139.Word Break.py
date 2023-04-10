# 解法1  使用DFS + Cache記憶 dp(i) 回傳True if s[i...n-1]  可以被分割成wordDict裡面的字串
from functools import lru_cache
class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        # 建立字典的hashtable 使查找加速
        word_set = set(wordDict)
        # 字串長度
        n = len(s)

        # 遞迴函式計算 lru_cache為緩存裝飾器  可為函式提供緩存功能
        @lru_cache(None)
        def dp(start):
            # 表示已經切割至尾部  直接返回TRUE
            if start == n:
                return True

            # n+1 用意在切割word時 s[start:end]並不包含end本身  故需+1
            for end in range(start+1, n+1):
                # 進行切割
                word = s[start:end]
                # 判斷是否符合
                if word in word_set and dp(end):
                    return True
            return False

        return dp(0)


test = Solution()
test.wordBreak("leetcode", ["leet", "code"])
