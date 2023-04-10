# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 解法1 先將頭尾串接起來  在移動指針到新的頭  再把前一個的鏈斷開
def rotateRight(head: ListNode, k: int) -> ListNode:
    # 驗證鏈結長度是否>=1
    if not head:
        return head

    # 當前指針位置
    cur = head
    # 指針長度
    length = 1
    # 遍歷鍊結  將cur設置在尾部並算出鏈結長度
    while cur.next:
        length += 1
        cur = cur.next
    #將頭尾連接
    cur.next = head

    # 計算需移動次數
    move_times = length - k % length
    # 進行指針移動
    for i in range(move_times):
        cur = cur.next

    # 新的頭部為cur.next 將頭尾斷開鏈結後 回傳new_head即為結果
    new_head = cur.next
    # 斷開頭尾鏈結
    cur.next = None

    return new_head
