#計算奇數字元 
def longestPalindrome(s: str) -> int:
    #奇數字元的陣列
    odd_list = []

    #遍歷s  找出奇數字元 反覆新增跟刪除  最後留下的即為奇數字元
    for string in s:
        if string in odd_list:
            odd_list.remove(string)
        else:
            odd_list.append(string)
    #迴文有兩種 moom沒有奇數字元的  以及 abcba 有一個奇數字元的
    #故最大回文長度為 字串長度 - (奇數個數 - 1 )
    return len(s) - max(0, len(odd_list) - 1)