# 解法1  使用遞迴並紀錄過程
# 記憶陣列 memo[i] 定義為範圍為 [i， n] 的子字串是否可以拆分，初始化為 -1，表示沒有計算過，如果可以拆分，則賦值為1，反之為0
class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        # 建立字典的hashtable 使查找加速
        word_set =  set(wordDict)
        # 記錄過程的結果 初始-1  
        memo = [-1 for _ in range(len(s))]

    # 遞迴函式 start為拆分字串位置
    def check(s: str, word_set: set, start: int, memo: list[int]) -> bool:
        


