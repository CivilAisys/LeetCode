#解法1 使用遞迴將所有可能串接
def letterCombinations(digits: str) -> list[str]:
    #號碼對應的字串 字串數字範圍為2-9
    digitDic = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z'],
    }

    #要回傳的結果
    result = []

    #傳進字串長度為零  直接回傳result
    if len(digits) == 0:
        return result
    #長度為1 回傳對應陣列
    if len(digits) == 1:
        return digitDic[digits[0]]

    firstDigit = digits[0:1]
    otherDigits = digits[1:]
    otherLetterCombinations = letterCombinations(otherDigits)
    firstDigitLetters = digitDic[firstDigit]

    for string in firstDigitLetters:
        for string1 in otherLetterCombinations:
            result.append(string + string1)

    return result


print(letterCombinations("23"))