/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
//解法1 同26題觀念 雙指標
var removeElement = function (nums, val) {
    /*  nextIndex用來辨別curIndex右邊 直到碰到不等於val的數 碰到不想等時 
        將nums[curIndex] = nums[nextIndex] 並將curIndex++ and nextIndex++ 
        且curIndex就等於不重複的數量    
    */
    let curIndex = 0, nextIndex = 0;

    while (curIndex < nums.length && nextIndex < nums.length) {
        if (nums[nextIndex] !== val) {
            nums[curIndex] = nums[nextIndex];
            curIndex++;
            nextIndex++;
        } else {
            nextIndex++
        }
    }

    return curIndex;
};

removeElement([3, 2, 2, 3], 3)