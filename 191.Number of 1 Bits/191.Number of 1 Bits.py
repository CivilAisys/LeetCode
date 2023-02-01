# 解法1 
def hammingWeight(n: int) -> int:
    count = 0
    while n:
        # 移位操作  讓n與1進行位元比對確認最後一位是否是1
        if (n & 1):
            count += 1
        n = n >> 1
    return count

