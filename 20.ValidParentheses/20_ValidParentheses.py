#解法1 開放括號(Opening bracket)最後進 
# 但其對應的閉合括號(Closing bracket)要最先出才會是合法的括號
def isValid(s: str) -> bool:
    #字串長度
    strLength = len(s)
    #長度 == 1 不合法
    if strLength == 1:
        return False

    #放置開放括號  當遇到閉合括號 pop出與其比對是否符合
    stack = []
    #存放封閉括號對應的開放括號
    bracketDic = {
        ")": "(",
        "}": "{",
        "]": "["
    }

    #迴圈比對字串
    for bracket in s:
        #表示為開放括號
        if bracket not in bracketDic:
            stack.append(bracket)
        else:
            if not stack:
                #當有閉合括號但stack無值  表示不合法
                return False
            elif stack and stack.pop() != bracketDic[bracket]:
                #閉合括號時 stack pop 與當前閉合比對是否一致         
                return False

    #需判斷stack若還有值  表示不合法
    if stack:
        return False
    
    return True




