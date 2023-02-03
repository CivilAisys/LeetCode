# 解法1 分別從左邊即右邊遍歷組成數字  相減=0即為迴文
def isPalindrome(x: int) -> bool:
    # 負數一定不為迴文
    if x < 0:
        return False
    # 轉換成字串
    string = str(x)
    # left right分別為string從左到右及從右到左的組成的結果
    left, right = '', ''
    # 左至右
    for i in range(len(string)):
        left += string[i]
    # 右至左
    for j in range(len(string) - 1, -1, -1):
        right += string[j]

    return (int(left) - int(right)) == 0

# 解法2 follow up:不能轉成字串
# 可以利用取整和取餘來獲得想要的數位，
# 比如 1221 這個數位，如果 計算 1221 / 1000， 則可得首位1，
# 如果 1221 % 10， 則可得到末尾1，進行比較，然後把中間的 22 取出繼續比較
def isPalindrome1(x: int) -> bool:
    if x < 0:
        return False
    # 用來取整數的值
    div = 1
    while x / div >= 10:
        div *= 10
    while x > 0:
        left = x // div
        right = x % 10
        if left != right:
            return False
        # x去掉頭尾的值  且一次去掉兩個數故div/100
        x = (x % div) // 10
        div /= 100

    return True

isPalindrome1(121)