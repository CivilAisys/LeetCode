# 解法1 使用兩個stack來維護 一個保存當前值  一個保存遍歷過的最小值  
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    def push(self, val: int) -> None:
        self.stack.append(val)
        # 若最小值存在的話就比較  沒有直接更新最小值
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
    # 需要判斷pop出去的是不是最小值 若是->更新最小值
    def pop(self) -> None:
        if self.stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()
    def top(self) -> int:
        return self.stack[-1]
    def getMin(self) -> int:
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()