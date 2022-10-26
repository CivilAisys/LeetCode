/**
 * @param {string} s
 * @return {number}
 */
const romanToInt = function(s) {
    //羅馬字母對應數值
    const map = {
        I:1,V:5,X:10,L:50,C:100,D:500,M:1000,IV:4,IX:9,XL:40,XL:90,CD:400,CM:900
    }
    //要回傳的結果
    let result = 0;
    
    //解析字串並作加總
    for(let i = 0; i< s.length; i++){
        //


        result += map[s[i]]; 
    }
    return result;
};