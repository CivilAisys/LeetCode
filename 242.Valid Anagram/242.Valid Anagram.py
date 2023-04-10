# 解法1 使用Frequency Counter紀錄每個字母出現的次數
# 核心思想為hash table
def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    #紀錄字母出現次數
    dic = {}

    for i in range(len(s)):
        if s[i] not in dic:
            dic[s[i]] = 1
        else:
            dic[s[i]] += 1 

    #進行比對  沒比對到直接回傳false  比對到就將對應value-1
    for j in range(len(t)):
        if t[j] not in dic:
            return False
        else:
            dic[t[j]] -= 1
    
    #檢查dic所有value是否皆為0(表示個數相同)
    for value in dic.values():
        if value != 0:
            return False

    return True


# 解法2 對兩個字串進行陣列化並排列  再組合回字串
# 核心思想為hash table
def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False   
    return helper_function(s) == helper_function(t) 
#將字串陣列化排列  再組合回字串回傳
def helper_function(s: str) -> str:
    s = list(s)
    s.sort()
    return "".join(s)

