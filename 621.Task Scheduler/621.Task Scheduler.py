from collections import Counter
# 解法1
# 滿足出現次數最多的任務數量  即可滿足任務的間隔要求 若有想同數量的兩種任務  則將兩個任務是為同一任務
# 找出最多次數的任務計算出單一任務最大次數most most-1為能夠區分的塊數 每塊的任務數為n+1(間隔+本身)
# (most-1) * (n+1) 為排除尾部的總個數  尾部個數則為最大次數的任務個數num_most
# ex: AAABBCD 2   most = 3 n = 2 num_most = 1 
# 結果為 max((most-1) * (n+1) + nums_most, len(tasks)) 若計算出值小於任務總個數則不符合 取任務個數長度
class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        count = Counter(tasks)
        # most_common(n) 回傳次數最多的n 個鍵值對(元組) [0][1] 為最大次數
        most = count.most_common()[0][1]
        num_most = len([i for i,v in count.items() if v == most])
        time = (most-1) * (n+1) + num_most
        return max(time, len(tasks))

test = Solution()
test.leastInterval(["A","A","A","B","B","B"], 2)