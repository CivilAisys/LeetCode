#解法1 使用兩個stack來保存字串 s and t的結果  最後把串起來  在兩兩比對是否相同
# 時間: O(n)  空間: O(n)
def backspaceCompare(s: str, t: str) -> bool:
    #保存兩字串結果
    stack1, stack2 = [], []
    # 只有當stack內有值且 當前字元== "#" 時 才要移除stack內字元 或當 i != "#" 及將當前字元加入至stack內
    for i in s:
        if stack1 and i == "#":
            stack1.pop()
        elif i != "#":
            stack1.append(i)

    for j in t:
        if stack2 and j == "#":
            stack2.pop()
        elif j != "#":
            stack2.append(j)

    return "".join(stack1) == "".join(stack2)



