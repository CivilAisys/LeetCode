/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
/*解法1(同15思維)  跑迴圈遍歷  需要雙層迴圈  
且條件為 i = 0 j = 1 k = length -1
並且i固定 j.k逐漸收縮  **前提是陣列經過排序**
**此題目可以不需要判別i,j,k前後可能相同問題  因為是回傳離target最近的  重複比對亦不會 造成影響**
*/
const threeSumClosest = function (nums, target) {
    //欲回傳結果 3數加總離target最近的回傳  
    //沒有指定初始  代表為undefined result為3數加總結果
    let result;
    //代表離target最短的距離  須取絕對值
    let minRange
    //排序
    nums.sort(compareNumbers);

    if (nums.length <= 3) {
        result = nums.reduce((num, value, index) => {
            return num += value;
        })
        return result;
    }
    //迴圈進行三數加總並比對
    for (let i = 0; i < nums.length; i++) {

        let j = i + 1;
        let k = nums.length - 1;
        while (k > j) {
            //三數加總 - target 並取絕對值
            let sum = nums[i] + nums[j] + nums[k];
            let sumMinusTarget = Math.abs((sum - target));

            //相減 = 0 代表3數加總等於target
            if (sumMinusTarget === 0) return target;

            //第一次跑時 result === undefind  直接附值並中斷此次while迴圈
            if (result === undefined) {
                result = sum;
                minRange = sumMinusTarget;
                k--
                continue;
            }

            //比對minRange && sumMinusTarget  等同比對距離 
            if (sumMinusTarget < minRange) {
                //距離小於minRange時需要進行result && minRange的更新
                result = sum;
                minRange = sumMinusTarget;
            }
            k--;
        }
    }
    return result;
};

//排序用
function compareNumbers(a, b) {
    return a - b;
}

//testcase threeSumClosest([4,0,5,-5,3,3,0,-4,-5], -2)