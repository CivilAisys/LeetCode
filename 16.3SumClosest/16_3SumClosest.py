# 解法1(同15思維)  跑迴圈遍歷  需要雙層迴圈  
# 且條件為 i = 0 j = 1 k = length -1
# 並且i固定 j.k逐漸收縮  **前提是陣列經過排序**
# 此題目可以不需要判別i,j,k前後可能相同問題  因為是回傳離target最近的  重複比對亦不會 造成影響**
def threeSumClosest(nums: list[int], target: int) -> int:
    #回傳結果  
    result = None
    #與target最短距離 依照距離判斷離target最近
    minRange = None
    #排序
    nums.sort()
    #陣列長度
    numsLength = len(nums)

    #長度等於3時  直接回傳3數加總
    if numsLength == 3:
        return sum(nums)
    
    #跑迴圈進行三數加總
    for index in range(numsLength):
        #index右側頭尾索引
        left = index + 1
        right = numsLength - 1
        while(right > left):
            #三數加總 - target並取絕對值
            total = nums[index] + nums[left] + nums[right]
            rangeOfSumMinusTarget = abs(total - target)

            #相減為0  直接回傳
            if rangeOfSumMinusTarget == 0:
                return target

            #第一次跑時 result == None 直接賦值並continue此次迴圈
            if result == None:
                result = total
                minRange = rangeOfSumMinusTarget
                #比較 sum 在 target左側還右側  來決定 left++ or right++ 並continue
                if total > target:
                    right -= 1
                else:
                    left += 1
                continue

            #比較rangeOfSumMinusTarget and minRange
            if  rangeOfSumMinusTarget < minRange:
                #當前距離小於minRange代表當前總和離target更近
                result = total
                minRange = rangeOfSumMinusTarget
            
            if total > target:
                right -= 1
            else:
                left += 1

    return result


threeSumClosest([0,0,0], 1)


