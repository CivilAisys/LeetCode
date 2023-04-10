# 首先遍曆一次矩陣，將值為0的點都存入佇列，將值為1的點改為INT_MAX。
# 這道題所有為0的點都是起點！然後開始BFS遍歷，從queue中取出一個數位，
# 遍歷其周圍四個點，如果越界或者周圍點的值小於等於當前值加1，則直接跳過。
# 因為周圍點的距離更小的話，就沒有更新的必要，否則將周圍點的值更新為當前值加1，然後把周圍點的座標加入queue
import collections
def updateMatrix(mat: list[list[int]]) -> list[list[int]]:
    m, n = len(mat), len(mat[0])
    # 構建與mat同樣形狀的矩陣
    dist = [[float('inf')]*n for _ in range(m)]
    q = collections.deque()
    # 找到mat內等於0的位置並押入佇列中並更新dist內的值
    for i in range(m):
        for j in range(n):
            if mat[i][j] == 0:
                dist[i][j] = 0
                q.append((i, j))

    # dirs保存上下左右的步數
    dirs = [[0, 1], [0, -1], [-1, 0], [1, 0]]
    while q:
        cur = q.popleft()
        for d in dirs:
            x = cur[0] + d[0]
            y = cur[1] + d[1]
            # 不越界且當前位置為1才進行比對及更新佇列
            if x >= 0 and x < m and y >= 0 and y < n and mat[x][y] == 1:
                # 表示dist[x][y]為1  並押入佇列下個迴圈再去對其位置做上下左右判斷
                if dist[x][y] > dist[cur[0]][cur[1]] + 1:
                    dist[x][y] = dist[cur[0]][cur[1]] + 1
                    q.append((x, y))

    return dist

updateMatrix([[0,0,0],[0,1,0],[0,0,0]])