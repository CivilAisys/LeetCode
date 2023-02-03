# 解法1
def reverseBits(n: int) -> int:
    res = 0
    for i in range(32):
        # 判斷最右端是否為1
        if n & 1:
            res += 1 << (31-i)
        # 右移繼續比對
        n >>= 1
    return res


reverseBits(964176192)
