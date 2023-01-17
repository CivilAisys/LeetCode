#解法1  先進行上下轉置 在進行[i][j] = [j][i] 對稱互換
#ex : 1 -> 2 -> 3       7 -> 8 -> 9       7 -> 4 -> 1
#     4 -> 5 -> 6  ->>  4 -> 5 -> 6  ->>  8 -> 5 -> 2
#     7 -> 8 -> 9       1 -> 2 -> 3       9 -> 6 -> 3
def rotate(matrix: list[list[int]]) -> None:
    # 上下轉置
    matrix.reverse()

    # 對矩陣進行對稱互換 避免重複替換  需紀錄替換過的位置  替換[i][j]  需紀錄[j][i] 以免再[j][i]時再次替換
    # 檢查 j in swapped_Dic[i] 若是 continue else swapped[j].append[i] 要反過來紀錄
    # 初始化swapped_Dic
    swapped_Dic = {}
    for i in range(len(matrix)):
        swapped_Dic[i] = []

    for i in range(len(matrix) - 1):
        for j in range(len(matrix[i])):
            if j in swapped_Dic[i]:
                continue
            else:
                swapped_Dic[j].append(i)
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

rotate([[2,29,20,26,16,28],[12,27,9,25,13,21],[32,33,32,2,28,14],[13,14,32,27,22,26],[33,1,20,7,21,7],[4,24,1,6,32,34]])