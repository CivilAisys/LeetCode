# 解法1  同54邏輯
def generateMatrix(n: int) -> list[list[int]]:
    # 使用List Comprehension產生相對應matrix 並其初始為0
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    # 計數器 也代表要更新matrix的值
    count = 1
    # 行列數
    row, col = len(matrix), len(matrix[0])
    # 左右上下索引
    left, right, top, bottom = 0, col-1, 0, row - 1

    # 終止條件為依賴count  故不須同54題在右下到左下左下到左上時不須判斷條件
    while count <= n*n:
        # 先從左上到右上
        for i in range(left, right+1):
            matrix[top][i] = count
            count += 1
        top += 1
        # 右上到右下
        for j in range(top, bottom+1):
            matrix[j][right] = count
            count += 1
        right -= 1
        # 右下到左下
        for k in range(right, left - 1, -1):
            matrix[bottom][k] = count
            count += 1
        bottom -= 1
        # 左下到左上
        for x in range(bottom, top - 1, -1):
            matrix[x][left] = count
            count += 1
        left += 1

    return matrix


# 解法2 搞不太懂
def generateMatrix1(n: int) -> list[list[int]]:
    A, lo = [[n*n]], n*n
    while lo > 1:
        lo, hi = lo - len(A), lo
        A = [list(range(lo, hi))] + list(zip(*reversed(A)))
    return A


print(generateMatrix1(3))
