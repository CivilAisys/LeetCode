
def divide(dividend: int, divisor: int) -> int:
    if (dividend == -2147483648 and divisor == -1): return 2147483647
    a, b, res = abs(dividend), abs(divisor), 0
    #右移幾位  就除2的幾次方  左移幾位  就乘2的幾次方
    for x in range(32)[::-1]:
        if (a >> x) - b >= 0:
            res += 1 << x 
            a -= b << x

    return res if (dividend > 0) == (divisor > 0) else -res

divide(10 ,3)