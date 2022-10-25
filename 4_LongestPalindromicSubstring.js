/* 給定字串長度n 含區間及其本身  共有n+n-1個中心點
只要遍歷這些中心點並且向左右拓展找新迴文  即可找到最大迴文 */
const longestPalindrome = function (str) {
    if (str === null || str.length < 1) return "";
    //最大回文結果
    let maxStr = '';

    for (let i = 0; i < str.length; i++) {
        //從1個字符擴展
        let str1 = expandAroundCenter(str, i, i);
        //從兩個字符中間擴展
        let str2 = expandAroundCenter(str, i, i + 1);
        //先比對str1 and str2 看誰比較長
        let currentMax = str1.length >= str2.length ? str1 : str2;
        //比對currentMax and MaxStr
        maxStr = currentMax.length > maxStr.length ? currentMax : maxStr;
    }
    return maxStr;
};

function expandAroundCenter(str, left, right) {
    //判斷當前索引最長回文樣貌
    let current = '';
    //條件: 不超出左右邊界  且遍歷的左右字元相同  代表找到迴文
    while (left >= 0 && right < str.length && str.charAt(left) === str.charAt(right)) {
        //subString 不包含end  故需right+1
        current = str.substring(left, right + 1);
        left--;
        right++;
    }

    //left-- and right++ 會使左右皆多出1個  故長度為 R-L-1
    return current;
}
