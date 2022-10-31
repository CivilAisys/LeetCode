/**
 * @param {number} n
 * @return {string[]}
 */ 
//解法1 遞迴求解  此題好難理解  此題為演算法中的 Backtracking(回溯法)
const generateParenthesis = function(n) {
    //要回傳的結果
    const result = [];

    /*當遞迴執行加入封閉括號時 會向下找尋結果  最後往上回到執行加入封閉括號的前一個結果  並以其為開頭向下執行 */
    const generate = (left, right, str) => {
        //開放及封閉括號相等代表一組解
        if(left === n && right === n){
            result.push(str);
            return;
        }
        
        if(left < n) generate(left+1,right,`${str}(`);
        if(left > right && right < n)generate(left,right+1, `${str})`);
    }
    //開放.封閉數量起始0 且傳入為空字串
    generate(0,0,'');

    return result;
};
