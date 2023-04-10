#解法1  使用二分搜尋法  須注意  此方法適用於以排列過的陣列
def search(nums: list[int], target: int) -> int:
    #左右索引
    left, right = 0, len(nums) - 1
    #需要 = 是因為可能傳入的nums內元素只有1個  也需要比對
    while left <= right:
        #中間索引 //代表相除後會取至整數  類math.floor
        mid = (left + right) // 2
        #比對target位於左側還是右側
        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            return mid

    return -1