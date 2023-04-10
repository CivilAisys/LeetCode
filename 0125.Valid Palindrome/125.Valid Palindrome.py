# 解法1  雙指標(頭尾)  先將傳入字串全變小寫
def isPalindrome(s: str) -> bool:
    # 將字串字母變小寫
    s = s.lower()
    # 左右指標
    left, right = 0, len(s) - 1

    while left < right:
        # 需判斷是否是英文字母
        if not s[left].isalnum():
            left += 1
        elif not s[right].isalnum():
            right -= 1
        elif s[left] != s[right]:
            # 比對s[left] 是否 == s[right]
            return False
        else:
            left += 1
            right -= 1

    return True


isPalindrome("A man, a plan, a canal: Panama")
