# 解析
# 1.讀取前導空白
# 2.讀取是否有'-' or '+'
# 3.讀取下一字元直到碰到非數值的字元或是結尾
# 4.數值須將開頭有0去除
# 5.數值不可超過界線*

def myAtoi(s: str) -> int:
    # 1.去除左側空白
    s = s.lstrip(" ")
    # 長度0時 回傳0
    if len(s) == 0:
        return 0

    # 存放數值字元
    result = ""
    # 2.辨別正負
    isNegative = True if s[0] == "-" else False
    # 3.遍歷字串直到碰到非數值的字元 正負號可能　++ +- -+等
    for index in range(len(s)):
        if checkStrignIsInteger(s[index]):
            result += s[index]
        else:
            if checkStringIsMinusOrPlus(s[index]) and index == 0:
                continue
            break

    # 未讀取到數值  返回0
    if len(result) == 0:
        return 0

    # 4.轉換result為數值
    result = int(result)
    # 5.判斷result的範圍
    if result > pow(2, 31) - 1 and not isNegative:
        return pow(2, 31) - 1
    elif result > pow(2, 31) and isNegative:
        return -pow(2, 31)

    return -result if isNegative else result


def checkStrignIsInteger(s: str) -> bool:
    return s.isdigit()


def checkStringIsMinusOrPlus(s: str) -> bool:
    return s == "+" or s == "-"


print(myAtoi("+-121"))
