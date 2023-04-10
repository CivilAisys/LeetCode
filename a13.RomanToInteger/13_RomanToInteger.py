# 解法1  1.先將字串IV.IX等特殊的解析並替換 2.解析替換後的字串作加總
def romanToInt(s: str) -> int:
    # 羅馬字母對應數值
    dic = {
        "I": 1, "V": 5, "X": 10, "L": 50,
        "C": 100, "D": 500, "M": 1000
    }
    # 加總結果
    result = 0

    # 解析並替換特殊組合
    s = s.replace("IV", "IIII").replace("IX", "VIIII")
    s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
    s = s.replace("CD", "CCCC").replace("CM", "DCCCC")

    # 遍歷解析過字串並加總
    for string in s:
        result += dic[string]

    return result
