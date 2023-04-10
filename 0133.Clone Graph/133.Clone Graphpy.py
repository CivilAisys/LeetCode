import collections
# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
# 解法1 DFS
# 在遞歸函數中，首先判空，然後再看當前的結點是否已經被克隆過了，若在 HashMap 中存在，
# 則直接返回其映射結點。否則就克隆當前結點，並在 HashMap 中建立映射，
# 然後遍歷當前結點的所有 neihbor 結點，調用遞歸函數並且加到克隆結點的 neighbors 陣列中即可
def cloneGraph(node: Node) -> Node:
    # 此dic保存複製過的節點 key為id(obj) value為物件
    dic = {}
    return helper(node, dic)
# 遞迴複製節點
def helper(node: Node, dic: dict) -> Node:
    # 沒有 or 複製過  直接返回
    if not node:
        return None
    if id(node) in dic:
        return dic[id(node)]
    # 複製節點
    clone = Node(node.val)
    dic[id(node)] = clone
    for neighbor in node.neighbors:
        clone.neighbors.append(helper(neighbor, dic))
    return clone

# 解法2 BFS
def cloneGraph1(node: Node)-> Node:
    if not node:
        return None
    # 此dic保存複製過的節點 key為id(obj) value為物件 
    # 使用deque輔助遍歷
    dic = {}
    deque = collections.deque()
    deque.append(node)
    clone = Node(node.val)
    dic[id(node)] = clone
    # 開始遍歷
    while deque:
        t = deque.popleft()
        # 遍歷節點的鄰居節點  若已被複製過直接加入至clone節點的鄰居節點內 
        # 若沒有 則複製並加入至dic並且加入至隊列中  若被複製過  其鄰居節點肯定也被複製過
        # 所以只有在沒被複製過情況下要加入至隊列
        for neighbor in t.neighbors:
            if id(neighbor) not in dic:
                dic[id(neighbor)] = Node(neighbor.val)
                deque.append(neighbor)
            # 無論鄰居節點有沒有複製過  當前遍歷節點的鄰居節點還是要加入
            dic[id(t)].neighbors.append(dic[id(neighbor)])

    return clone




a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.neighbors = [b, d]
b.neighbors = [a, c]
c.neighbors = [b, d]
d.neighbors = [a, c]

cloneGraph1(a)
