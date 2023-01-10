#解法1 比對陣列內不重複  且不重複個數k需對應nums內前k個數都不重複
def removeDuplicates(nums: list[int]) -> int:
    #result = numsLength(去重後) 且至少為1
    result = 1
    #比對前後索引
    curIndex = 0
    nextIndex = 1

    #比對nums[i] == nums[j]
    while curIndex < len(nums) and  nextIndex < len(nums):
        #前後相等 curIndex不需要+1 nextIndex+1繼續比對至不重複為止
        if nums[curIndex] == nums[nextIndex]:
            nextIndex += 1
        else:
        #不重複時curIndex+1 and result+1 並將nums[curIndex]指定為nums[nextIndex] 且nextIndex+1
            result += 1
            curIndex += 1
            nums[curIndex] = nums[nextIndex]
            nextIndex += 1
            
    return result

removeDuplicates([1,1,2])






