#解法1 逆波蘭表達式就是把操作數放前面，把操作符後置的一種寫法
# 從前往後遍歷陣列，遇到數位則壓入棧中，遇到符號，則把棧頂的兩個數位拿出來運算，把結果再壓入棧中
def evalRPN(tokens: list[str]) -> int:
    if len(tokens) == 1:
        return int(tokens[0])
    stack = []

    for token in tokens:
        if token != '+' and token != '-' and token != '/' and token != '*':
            #數字壓入stack中
            stack.append(token)
        else:
            #非數字就拿stack上面兩數進行運算
            num1 = int(stack.pop())
            num2 = int(stack.pop())
            if token == '+':
                stack.append(num2 + num1)
            elif token == '-':
                stack.append(num2 - num1)
            elif token == '*':
                stack.append(num2 * num1)
            elif token == '/':
                stack.append(num2 / num1)
    #避免有0.0 故回傳需再轉為int  0/3 = 0.0
    return int(stack.pop())

evalRPN(["0","3","/"])