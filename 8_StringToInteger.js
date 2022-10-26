/**
 * @param {string} s
 * @return {number}
 */
/*解析 
1.讀取前導空白 
2.讀取是否有'-' or '+' 
3.讀取下一字元直到碰到非數值的字元或是結尾 
4.數值須將開頭有0去除
5.數值不可超過界線*/
//解法1
const myAtoi = function (s) {
    //結果存放遍歷的數值字元
    let result = '';
    //辨別是否正負
    let isNegative = false;

    //1.去除空白
    let str = s;
    str = str.trim();

    //遍歷字串  從索引1開始
    for (let i = 0; i < str.length; i++) {
        //3.辨別是否為數值
        if (checkStringIsInteger(str[i])) {
            //是 -> 串接字串result
            result += str[i];
        } else {
            //否 -> break  直接跳離迴圈
            //2.辨別正負 若是 + or - 則繼續迴圈  否 -> 跳離迴圈
            //限定 i===0 因為傳進字串可能+-連續  連續的話  直接跳出
            if (checkStringIsMinusOrPlus(str[i]) && i === 0) {
                isNegative = str[i] === '-' ? true : false;
                continue;
            }
            break;
        }
    }
    //若未讀取到數值  回傳0
    if (result.length === 0) return 0;

    //4.轉換result為數值
    result = Number(result);

    //5.判斷result的範圍
    if (result > Math.pow(2, 31) - 1 && !isNegative) {
        return Math.pow(2, 31) - 1;
    } else if (result > Math.pow(2, 31) && isNegative) {
        return -Math.pow(2, 31);
    }

    return isNegative ? -result : result;
};
//檢查傳進字串是否回數值
function checkStringIsInteger(str) {
    //Number(str) str若為空白 會回傳0
    if (Number.isInteger(Number(str)) && str !== " ") {
        return true;
    } else {
        return false;
    }
}
//檢查傳進的字串是否為- or +
function checkStringIsMinusOrPlus(str) {
    let result = false;
    if (str === '-') {
        result = true
    } else if (str === '+') {
        result = true;
    }
    return result;
}