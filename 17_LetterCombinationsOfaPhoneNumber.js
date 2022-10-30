/**
 * @param {string} digits
 * @return {string[]}
 */
//解法1 使用遞迴將所有可能串接
const letterCombinations = function (digits) {
    //號碼對應的字串 字串數字範圍為2-9
    const digitMap = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z'],
    };

    //要回傳的結果陣列
    const result = [];

    //傳進字串長度為零  直接回傳result
    if (digits.length === 0) return result
    //長度為1  直接回串對應陣列
    if (digits.length === 1) return digitMap[digits[0]];

    //長度為1  直接回串對應陣列
    if (digits.length === 1) return digitMap[digits[1]];

    //遞迴
    const firstDigit = digits.slice(0, 1);
    const otherDigits = digits.slice(1);
    const otherLetterCombinations = letterCombinations(otherDigits);
    const firstDigitletters = digitMap[firstDigit];
    //要回傳的結果陣列
    let resultArr = [];
    firstDigitletters.forEach(item1 => {
        otherLetterCombinations.forEach(item2 => {
            resultArr.push(item1 + item2);
        })
    })

    return resultArr;
};
