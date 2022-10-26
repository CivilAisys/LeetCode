/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
//解法1
const twoSum = function (nums, target) {
    //結果的陣列
    let result = [];
    //跑巢狀迴圈加總  加總=target  回傳結果
    for (let i = 0; i < nums.length; i++) {
        for (let j = i + 1; j < nums.length; j++) {
            if ((nums[i] + nums[j]) === target) {
                result.push(i);
                result.push(j);
                return result;
            }
        }
    }
    return result;
};

//解法2
const twoSumV2 = (nums, target) => {
    //使用obj  可將巢狀迴圈縮減
    let map = {};

    for(let i = 0; i < nums.length; i++){
        //將target - 對應元素
        let minus = target - nums[i];
        
        //若是相減完的結果在map內  return結果
        if(minus in map){
            return[map[minus], i]
        }
        //若未比對到  key為值 value為他在nums內的索引
        map[nums[i]] = i;
    }
    return null;
}