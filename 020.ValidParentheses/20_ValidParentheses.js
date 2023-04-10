/**
 * @param {string} s
 * @return {boolean}
 */

//解法1 開放括號(Opening bracket)最後進但是應該要最先出才會是合法的括號
const isValid = function (s) {
    if (s.length <= 1) return false;

    //1.遇到開放的括號  放進arr(stack)內 
    let stack = [];
    //存放封閉括號對應的開放括號
    let bracketMap = {
        ")": "(",
        "}": "{",
        "]": "["
    }

    /*跑迴圈 遇到開放括號就加入stack  
    遇到封閉的括號就對stack pop 來比對是否一致*/
    for (let i = 0; i < s.length; i++) {
        if (s[i] === "(" || s[i] === "{" || s[i] === "[") {
            stack.push(s[i]);
        } else {
            //對stack pop 並與s[i]比對是否一致
            if (stack.pop() !== bracketMap[s[i]]) return false;
        }
    }

    //需確認stack內是否還有值  若有 return false
    if (stack.length > 0) return false;

    return true;
};

//解法2

const isValid2 = function (s) {

    if (s.length == 0 || s.length % 2 != 0) {
        return false;
    }

    const closingParentheses = {
        "(": ")",
        "{": "}",
        "[": "]"
    }

    const stack = [];

    for (let i = 0; i < s.length; i++) {
        if (s[i] in closingParentheses) {
            stack.push(s[i]);
        } else if (s[i] != closingParentheses[stack.pop()]) {
            return false;
        }
    }

    return stack.length === 0;
}