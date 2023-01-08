/**
 * @param {number} num
 * @return {string}
 */
//解法1  map存放所有可能並從大到小排列  對map跑迴圈並取餘數
const intToRoman = function(num) {
    //物件對應字母及其值
    const map = {
        M: 1000, CM: 900, D: 500, CD: 400,
        C: 100, XC: 90, L: 50, XL: 40, X: 10,
        IX: 9, V: 5, IV: 4, I: 1
    };
    //Object.entries 回傳 陣列內陣列 ex: [[key or index,value]]
    //reduce(sum, [a, b])  [a,b] 為es6解構附值
    return Object.entries(map).reduce((result, [letter, value]) => {
        // String.repeat(times) 會回傳呼叫對應字串次數(times)  回傳幾次使用Math.floor取整數
        result += letter.repeat(Math.floor(num/value));
        //num 取餘數
        num %= value;

        return result;
    }, '')

};