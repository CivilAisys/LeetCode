class Solution:
    def decodeString(self, s: str) -> str:
        # stack用於暫存中間結果 
        stack = []
        currNum = 0
        currString = ''

        # 對字符串進行遍歷
        for char in s:
            if char.isdigit():
                # 此操作作用為多位數字可轉換為對應的整數值
                currNum = currNum * 10 + int(char)
            elif char == '[':
                # 當前字符是左方括號'['，表示遇到了一個新的重複序列的開始。將currString和currNum壓入stack中，
                # 並將currString和currNum重置為空字符串和零，以準備處理新的重複序列。
                stack.append(currString)
                stack.append(currNum)
                currString = ''
                currNum = 0
            elif char == ']':
                num = stack.pop()
                prevString = stack.pop()
                currString = prevString + num * currString
            else:
                currString += char
        
        return currString

test = Solution()
test.decodeString("2[abc]3[cd]ef")