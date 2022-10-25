/**
 * @param {string[]} strs
 * @return {string}
 */
const longestCommonPrefix = function (strs) {
    //傳入字串沒有內容  回傳""
    if (strs.length === 0) return "";
    //以第一個當作基準來做比較並以其當作回傳結果
    let prefix = strs[0];

    //迴圈進行比對
    for (let i = 1; i < strs.length; i++) {
        //使用整個字串的內容去做比對  沒有比對到prefix內容長度就-1
        // !== 0 因為比對結果應該從開頭 比對到的值索引必須為0 表示為開頭  prefix的值越比對應該會越小
        while (strs[i].indexOf(prefix) !== 0) {
            prefix = prefix.substring(0, prefix.length - 1);
            //prefix length==0代表沒有比對到  估回傳""
            if (prefix.length === 0) return "";
        }
    }
    return prefix;
};