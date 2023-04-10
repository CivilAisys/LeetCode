/**
 * @param {number} x
 * @return {boolean}
 */
//解法1分別從左邊即右邊遍歷組成數字  相減=0即為迴文
const isPalindrome = function (x) {
    //負數一定不為迴文
    if (x < 0) return false;
    let result = false;

    let str = x.toString();
    //left為左向右組成的數字  反之
    let left = '', right = '';
    //由左向右遍歷
    for (let i = 0; i < str.length; i++) {
        left += str[i];
    }
    //由右向左遍歷
    for (let i = str.length - 1; i >= 0; i--) {
        right += str[i];
    }
    result = (Number(left) - Number(right)) === 0 ? true : false;
    return result;
};

//解法2 遞迴從左右端點遍歷比對 每次遞迴僅比對頭尾端點
const isPalindrome2 = function (x) {
    const str = x.toString();
    //長度 === 1  代表傳進字串為迴文
    if (str.length === 1) return true;
    //起始索引
    const start = str[0];
    //最後索引
    const end = str[str.length - 1];

    if (start !== end) return false;

    //若是經過前面判斷尚未回傳false  此時若字串長度為2  此字串即為迴文
    if (str.length === 2) return true;

    //比對完成切割字串
    let subStr = str.substring(1, str.length - 1);
    return isPalindrome2(subStr);
}
