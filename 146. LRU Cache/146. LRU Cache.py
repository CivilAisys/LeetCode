# 雙向鏈表
class ListNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
# 解法1 使用雙向鏈表 + hashtable 實現LRU Cache
# 雙向鏈表為維護順序的資結  剛使用的放到鏈表頭部  一直未被使用的放到鏈表尾部 當達到容量時  從尾部刪除
# 鏈表的get時間複雜度為 O(N)  故使用hashtable(dict)進行優化為題目要求的O(N)
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        # 使用dict來存對應的node {key,node}
        self.cache = {}
        self.head = ListNode()
        self.tail = ListNode()
        # dummy head and tail 需要有頭尾的指針對應 因為需要有移到尾及去除頭的操作
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1 
        # 先移除 在將其移動至尾部
        node = self.cache[key]
        self.remove_node(node)
        self.move_to_tail(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        # old key
        if self.get(key) != -1: 
            self.cache[key].value = value
            return

        # new key
        if len(self.cache) >= self.capacity :
            self.remove_head()
        node = ListNode(key, value)
        self.move_to_tail(node)
        self.cache[key] = node

    ### 雙相鏈結操作
    # 移除節點
    def remove_node(self, node: ListNode) -> None:
        node.prev.next = node.next 
        node.next.prev = node.prev 

    # 移動至尾部
    def move_to_tail(self, node: ListNode) -> None:
        node.prev = self.tail.prev # tail.prev <- node
        node.next = self.tail # node -> tail

        node.prev.next = node # tail.prev -> node
        self.tail.prev = node # node <- tail

    # 移除頭部
    def remove_head(self) -> None:
        node = self.head.next
        self.remove_node(node)
        self.cache.pop(node.key)

