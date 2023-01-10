# 解法1 同26題觀念 雙指標
def removeElement(nums: list[int], val: int) -> int:
    #  nextIndex用來辨別curIndex右邊 直到碰到不等於val的數 碰到不想等時
    # 將nums[curIndex] = nums[nextIndex] 並將curIndex++ and nextIndex++
    # 且curIndex就等於不重複的數量
    curIndex = 0
    nextIndex = 0
    numsLength = len(nums)

    while (curIndex < numsLength and nextIndex < numsLength):
        if nums[nextIndex] != val:
            nums[curIndex] = nums[nextIndex]
            curIndex += 1
            nextIndex += 1
        else:
            nextIndex += 1

    return curIndex
