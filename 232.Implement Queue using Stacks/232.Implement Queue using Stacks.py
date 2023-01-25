# 解法1 使用2個stack
# 因為stack FILO  quene FIFO
class MyQueue:
    # new_stack進行緩存使用 等到要peek pop時 
    # 確認old內是否還有資料  若沒有  才將new內的資料倒入old
    def __init__(self):
        self.old_stack = []
        self.new_stack = []
    # push
    def push(self, x: int) -> None:
        self.new_stack.append(x)
    #使用pop時  先清空new內的緩存值
    def pop(self) -> int:
        self.shift_stack()
        return self.old_stack.pop()
    #使用peek時  先清空緩存再回存 old_stack的最後一個
    def peek(self) -> int:
        self.shift_stack()
        return self.old_stack[-1]
    #需要old跟new皆為空時才是真正的空quene
    def empty(self) -> bool:
        return not self.new_stack and not self.old_stack
    #old為空才進行轉移
    def shift_stack(self) -> None:
        if self.old_stack:
            return
        while self.new_stack:
            self.old_stack.append(self.new_stack.pop())
    