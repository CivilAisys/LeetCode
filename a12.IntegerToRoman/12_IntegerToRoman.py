import math
# 解法1  map存放所有可能並從大到小排列  對map跑迴圈並取餘數


def intToRoman(num: int) -> str:
    result = ""
    # 物件對應字母及其值
    dic = {
        "M": 1000, "CM": 900, "D": 500, "CD": 400,
        "C": 100, "XC": 90, "L": 50, "XL": 40, "X": 10,
        "IX": 9, "V": 5, "IV": 4, "I": 1
    }

    # 遍歷dic
    for key in dic:
        result += key * math.floor(num/dic[key])
        # 取餘數
        num %= dic[key]

    return result
