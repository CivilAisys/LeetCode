#解法1 使用hash table計算magzine字元出現次數 在與ransomNote進行比對
def canConstruct(ransomNote: str, magazine: str) -> bool:
    #計算字元出現次數 使用dict
    dic = {}
    for string1 in magazine:
        if string1  in dic:
            dic[string1] += 1
        else:
            dic[string1] = 1

    #進行比對
    for string2 in ransomNote:
        if string2 not in dic:
            #若不在dic內 回傳False
            return False
        else:
            dic[string2] -= 1
        #將出現次數-1 若<0代表出現次數超過 回傳False
        if dic[string2] < 0:
            return False
    return True

canConstruct('aa','aab')