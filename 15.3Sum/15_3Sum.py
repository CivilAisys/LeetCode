# 解法1 且條件為 i = 0 j = 1 k = length -1
# 並且i固定 j.k逐漸收縮(且i,j,k遇到前後相同需跳過  避免重複)
#  **前提是陣列經過排序**
def threeSum(nums: list[int]) -> list[list[int]]:
    # 回傳結果
    result = []
    # 排序
    nums.sort()
    # 陣列長度
    numsLength = len(nums)

    for index in range(numsLength):
        # index < numsLength -2 的情況下才會進行比對
        if index < numsLength - 2:
            # 若是 index > 0 且 nums[index] == nums[index - 1]直接跳過此次迴圈
            if index > 0 and nums[index] == nums[index - 1]:
                continue

            # left and right為 i 右側的頭尾索引
            left = index + 1
            right = numsLength - 1
            # left != right != index
            while (right > left):
                # 三數加總
                sum = nums[index] + nums[left] + nums[right]
                # 若是sum > 0 right需-1 sum < 0 left需+1  此前提為陣列經過排序  順序為從小到大
                if sum == 0:
                    result.append([nums[index], nums[left], nums[right]])

                    # 須避開 nums[right] = nums[right-1] 和 nums[left] = nums[left+1]
                    # 的情況  避免result會有重複的陣列 需要有rigth >left  避免[0,0,0]這樣的情況
                    while nums[right] == nums[right - 1] and right > left:
                        right -= 1
                    while nums[left] == nums[left + 1] and right > left:
                        left += 1

                    # sum == 0  固定需 left++ right--
                    left += 1
                    right -= 1
                elif sum > 0:
                    right -= 1
                elif sum < 0:
                    left += 1
    return result

print(threeSum([0, 0, 0]))
