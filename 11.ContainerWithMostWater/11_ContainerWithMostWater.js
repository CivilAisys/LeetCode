/**
 * @param {number[]} height
 * @return {number}
 */

//解法1 跑巢狀雙層迴圈 計算每一個可能的容積 此方法會超時
const maxArea = function (height) {
    //最大體積(結果)
    let maxVoulume = 0;
    //跑迴圈計算最大體積
    for (let i = 0; i < height.length; i++) {

        for (let j = i + 1; j < height.length; j++) {
            maxVoulume = Math.max(maxVoulume, Math.min(height[i], height[j]) * (j - i))
        }
    }
    return maxVoulume;
};


//解法2 從頭尾開始計算容積  逐漸向內縮小 且須比較左右兩端點高度 較低的向內縮進
const maxArea2 = function (height) {
    //最大體積(結果)
    let maxVoulume = 0;
    //頭尾的索引值
    let left = 0;
    let right = height.length - 1;
    //迴圈條件 right > left
    while (right > left) {
        maxVoulume = Math.max(maxVoulume, Math.min(height[left], height[right]) * (right - left));
        if (height[right] > height[left]) {
            left++;
        } else {
            right--;
        }
    }
    return maxVoulume;
}