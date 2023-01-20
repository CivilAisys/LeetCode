# 解法1 將字串右側空白去掉  在從最後一個開始遍歷直到碰到" " 遍歷次數及未最後字串長度
def lengthOfLastWord(s: str) -> int:
    # 將右側空白去掉 並在左側將上1個空白  避免左側無空白
    s = s.rstrip(" ")
    s = " " + s
    # 最後字串長度
    length_of_last_string = 0
    # 倒著遍歷回來
    for index in range(len(s) - 1, -1, -1):
        if s[index] == " ":
            return length_of_last_string
        else:
            length_of_last_string += 1


lengthOfLastWord("d")
