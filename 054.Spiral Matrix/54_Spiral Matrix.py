# 解法1
def spiralOrder(matrix: list[list[int]]) -> list[int]:
    # 先算出行列
    rows = len(matrix)
    cols = len(matrix[0])
    # 結果
    result = []

    # 左右上下
    left, right, top, bottom = 0, cols - 1, 0,  rows - 1

    # 迴圈條件為
    while left <= right and top <= bottom:
        # range(i,j) 不包含 j 故需+1
        # 左上到右上  一個迴圈表示一個row完成 top需-1
        for i in range(left, right+1):
            result.append(matrix[top][i])
        top += 1

        # 右上到右下  一個迴圈表示一個col完成 right需 -1
        for j in range(top, bottom + 1):
            result.append(matrix[j][right])
        right -= 1

        # 右下到左下  需判斷 top<=bottom   迴圈跑完表示完成一個row bottom需+1
        if top <= bottom:
            for k in range(right, left-1, -1):
                result.append(matrix[bottom][k])
            bottom -= 1

        # 左下到左上 需判斷left <= right  迴圈跑完表示完成一個col left 需+1
        if left <= right:
            for x in range(bottom, top - 1, -1):
                result.append(matrix[x][left])
            left += 1
    return result


print(spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
