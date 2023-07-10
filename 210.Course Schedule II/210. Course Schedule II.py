from collections import deque
# 使用拓樸排序 拓樸排序適用於有先後關係的順序當中  先從入度為0的開始遍歷
class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        # 初始化入度及鄰接列表
        in_degrees = [0] * numCourses
        adjacency = [[] for _ in range(numCourses)]

        # 建立入度及鄰接列表
        for cur, pre in prerequisites:
            in_degrees[cur] += 1
            adjacency[pre].append(cur)

        # 將入度為0的節點加入佇列(拓樸排序用)
        queue = deque()
        for i in range(numCourses):
            if in_degrees[i] == 0:
                queue.append(i)
        
        # 進行拓樸排序
        result = []
        while queue:
            pre = queue.popleft()
            result.append(pre)
            # 將相鄰節點入度減1  且若入度為0  加入佇列queue中進行遍歷
            for cur in adjacency[pre]:
                in_degrees[cur] -= 1
                if in_degrees[cur] == 0:
                    queue.append(cur)

        # 修課完成返回結果 不然即返回空列表
        if len(result) == numCourses:
            return result
        else:
            return []

