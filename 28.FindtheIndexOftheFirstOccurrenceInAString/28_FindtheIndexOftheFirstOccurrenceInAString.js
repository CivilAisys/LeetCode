/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
//解法1 暴力比對  時間複雜度為O(nm) n為hatstack.length m為needle.length
var strStr1 = function (haystack, needle) {
    let mainStrLength = haystack.length;
    let patternLength = needle.length;
    for (let i = 0; i < mainStrLength; i++) {
        //從主字串發起點與比對字串首位開始嘗試比對
        let a = i, b = 0;
        while (b < patternLength && haystack[a] === needle[b]) {
            a++;
            b++;
        }
        //當比對字串的索引與其長度一樣時  表示完整比對到  回傳i
        if(b === patternLength) return i;
    }
    return -1;
};



//解法2  此題最佳解為KMP算法
var strStr1 = function(haystack, needle) {
    




};

//計算KMP中的關鍵  next數組  次長共同前後綴(LPS)
function getNext(str){
    next
}

getNext("abcab")

