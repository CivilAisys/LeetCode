#解法1  先進行上下轉置 在進行[i][j] = [j][i] 對稱互換
#ex : 1 -> 2 -> 3       7 -> 8 -> 9       7 -> 4 -> 1
#     4 -> 5 -> 6  ->>  4 -> 5 -> 6  ->>  8 -> 5 -> 2
#     7 -> 8 -> 9       1 -> 2 -> 3       9 -> 6 -> 3
def rotate(matrix: list[list[int]]) -> None:
    #上下轉置
    matrix.reverse()

    #對矩陣進行對稱互換

    for i in range(len(matrix) - 1):
        for j in range(len(matrix[i])):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    print(matrix)


rotate([[1,2,3],[4,5,6],[7,8,9]])