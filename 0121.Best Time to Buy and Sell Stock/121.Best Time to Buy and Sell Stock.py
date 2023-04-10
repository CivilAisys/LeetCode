import math
# 解法1  遍歷數組  紀錄當前遍歷到的數值與此前出現過最低的值進行比對紀錄獲利最大的值
def maxProfit(prices: list[int]) -> int:
    # 最低買進的值(需先設置為最大 避免錯誤設置買進價格)  及最大獲利
    buy = math.inf
    max_profit = 0

    for index in range(len(prices)):
        # 更新最低價格  並計算最大獲利(當前價格-出現的最低價格)
        buy = min(buy, prices[index])
        max_profit = max(max_profit, prices[index] - buy)

    return max_profit
