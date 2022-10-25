/* 給定字串長度n 含區間及其本身  共有n+n-1個中心點
只要遍歷這些中心點並且向左右拓展找新迴文  即可找到最大迴文 */
const longestPalindrome = function (str) {
    if (str === null || str.length < 1) return "";
    //計算此迴文的起始及結束
    let start = 0, end = 0;
    for (let i = 0; i < str.length; i++) {
        //從1個字符擴展
        let length1 = expandAroundCenter(str, i, i);
        //從兩個字幅中間擴展
        let length2 = expandAroundCenter(str, i, i + 1);
    }
    return s;
};

const expandAroundCenter = function (str, left, right) {
    while (left >= 0 && right < str.length && str.charAt(left) === str.charAt(right)) {
        left--;
        right++;
    }
}
