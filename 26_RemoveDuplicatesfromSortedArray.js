/**
 * @param {number[]} nums
 * @return {number}
 */
//解法1  迴圈比對前後值是否相同 並使用splice來刪除原陣列的值  此題限制不能指定其他arr變數 而是要直接變更原陣列
const removeDuplicates = function(nums) {
    let i = 0;
    while(i < nums.length -1){
        if(nums[i] === nums[i+1]){
            nums.splice(i+1,1);
        } else{
            i++;
        }
    }

    return nums.length;
};

//解法2 
const removeDuplicates2 = function(nums) {
    // result 至少為1 
    let result = 1, i = 0, j = 1;
    while(i < nums.length && j < nums.length) {
        /*當相等的有複數個時 j是為了比對當前有多少個相同的值  在比對到的時候  將最後一個相同的值改變為新比對到的不同數值以此持續推進
        且將result+1*/
        if(nums[j] === nums[i]) {
            j++;
        } else {
            result += 1;
            i++;
            nums[i] = nums[j];
            j++;
        }
    }
    
    return result;
};