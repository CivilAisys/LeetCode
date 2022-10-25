/**
 * @param {number} x
 * @return {number}
 */
const reverse = function (x) {
    //先將傳進來的數字取絕對值並轉換成string 附值給result
    let result = Math.abs(x).toString();
    //是否是負數
    let isNegative = x > 0 ? false : true;
    //spilt -> array join -> string  
    result = result.split("").reverse().join("");
    //轉換完避免開頭為0  使用javascript Number物件若傳進開頭為0  會自動刪除
    result = Number(result);

    //超出最大最小範圍須回傳0
    if (!isNegative && result > Math.pow(2, 31) - 1) {
        return 0;
    } else if (isNegative && result > Math.pow(2, 31)) {
        return 0;
    }
    return isNegative ? -result : result;
};