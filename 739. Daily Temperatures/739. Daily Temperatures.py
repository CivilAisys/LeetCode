# 解法1 使用棧輔助
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        res = [0] * len(temperatures)  # 初始化結果陣列  初始值為0
        stack = []  # 使用stack來存放尚未找到溫度更高的日期

        # 遍歷溫度數組
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                # 若stack不為空 且當前溫度比棧頂溫度高  那就可以彈出
                idx = stack.pop()
                res[idx] = i - idx
            stack.append(i)
        return res
