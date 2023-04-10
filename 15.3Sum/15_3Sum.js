/**
 * @param {number[]} nums
 * @return {number[][]}
 */
/*解法1  跑迴圈遍歷  需要雙層迴圈  
且條件為 i = 0 j = 1 k = length -1
並且i固定 j.k逐漸收縮(且i,j,k遇到前後相同需跳過  避免重複)  **前提是陣列經過排序**
*/
const threeSum = function (nums) {
    //要回傳的結果
    let results = [];
    //排序
    nums.sort(compareNumbers);

    for (let i = 0; i < nums.length - 2; i++) {

        //須避免 i = i - 1的情況 避免重複跑
        if (i > 0 && nums[i] === nums[i - 1]) continue;

        // j.k 表示 i 右側的頭尾索引值
        let j = i + 1;
        let k = nums.length - 1
        // i j k 不相等  故此迴圈條件 k > j
        while (k > j) {
            let sum = nums[i] + nums[j] + nums[k];
            //若是sum > 0 k需-1 sum < 0  j需+1
            if (sum === 0) {
                results.push([nums[i], nums[k], nums[j]]);

                /**需要避開 k = k - 1 j = j + 1的情況 
                也就是前後重複  會導致result有相同的陣列*/
                while (nums[k] === nums[k - 1]) k--;
                while (nums[j] === nums[j + 1]) j++;

                //比對為0  固定需k-- j++
                k--;
                j++;
            } else if (sum > 0) {
                k--;
            } else if (sum < 0) {
                j++;
            }
        }
    }

    return results;
};

//排序用
function compareNumbers(a, b) {
    return a - b;
}