def reverse(x: int) -> int:
    # 先將傳進數值取絕對值並轉為字串  字串才可遍歷每個字元
    result = str(abs(x))
    # 判斷是否為負數
    isNegative = True if x < 0 else False
    # 反轉字串
    result = result[::-1]
    # 轉成int
    result = int(result)

    # 超出最大範圍須回傳0
    if not isNegative and result > pow(2, 31) - 1:
        return 0
    elif isNegative and result > pow(2, 31):
        return 0
    return -result if isNegative else result
