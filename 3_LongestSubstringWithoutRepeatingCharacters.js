/**
 * @param {string} s
 * @return {number}
 */
const lengthOfLongestSubstring = function (s) {
    //此用來存放每一個字元最後出現的索引
    const map = {};
    //此為當前不重複字串的開頭索引
    let left = 0;

    //將傳進字串切割變為陣列 like['a','b','c']
    return s.split('').reduce((max, value, index) => {
        /*比較每個字元出現的索引是否已經有值且大於等於 開頭索引  map[index]  不為undefined時 代表重複  故須以當前字元索引+1 
         *當作此切割字串的開頭索引
         */
        left = map[value] >= left ? map[value] + 1 : left;

        //紀錄每個字元當前最新的索引
        map[value] = index
        //比較max  與字串長度並回傳
        return Math.max(max, index - left + 1);
    }, 0)
};