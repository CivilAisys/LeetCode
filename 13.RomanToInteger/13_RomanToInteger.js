/**
 * @param {string} s
 * @return {number}
 */
//解法1  1.先將字串IV.IX等特殊的解析並替換 2.解析替換後的字串作加總
const romanToInt = function (s) {
    //羅馬字母對應數值
    const map = {
        I: 1, V: 5, X: 10, L: 50, C: 100, D: 500, M: 1000
    }
    //要回傳的結果
    let result = 0;

    //將字串解析並替換
    s = s.replace('IV', 'IIII').replace('IX', 'VIIII');
    s = s.replace('XL', 'XXXX').replace('XC', 'LXXXX');
    s = s.replace('CD', 'CCCC').replace('CM', 'DCCCC');

    //遍歷替換後的字串
    for(let i = 0; i< s.length; i++){
        result += map[s[i]];
    }
    return result;
};