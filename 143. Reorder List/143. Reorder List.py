# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        # 使用快慢指針找到鏈表的終點
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 將鏈表後半部逆轉
        prev = None  # 前一個節點
        curr = slow.next  # 當前節點
        slow.next = None  # 將前半部分鏈表斷開
        # 開始逆轉
        while curr:
            next_node = curr.next  # 先保存下個節點
            curr.next = prev  # 將當前節點指向前一個節點(逆轉)
            prev = curr  # 前一個節點後移
            curr = next_node  # 當前節點後移

        # 將前後鏈表交錯合併
        p1 = head
        p2 = prev
        while p2:
            # 保存下個節點
            next_p1 = p1.next
            next_p2 = p2.next
            # 交錯
            p1.next = p2
            p2.next = next_p1
            # 移至下個節點
            p1 = next_p1
            p2 = next_p2
