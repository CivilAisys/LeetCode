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

//解法2 因為spile為遍歷 套在while內會使效能非常慢 所以只要直接紀錄不重複的數字有幾個
const removeDuplicates2 = function(nums) {
    let result = 1, i = 0, j = 1;
    debugger
    while(i < nums.length && j < nums.length) {
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