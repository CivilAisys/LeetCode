# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # 終止條件  若只有head或是沒有節點  直接返回
        if not head or not head.next:
            return head

        # 使用快慢指針找到鏈表中心
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 斷開鏈表為兩部分
        mid = slow.next
        slow.next = None

        # 遞迴排序兩部分鏈表
        left = self.sortList(head)
        right = self.sortList(mid)

        return self.merge(left, right)

    def merge(self, left, right) -> ListNode:
        dummy = ListNode(0)  # 哨兵節點
        curr = dummy  # 當前節點

        # 合併兩個鏈表
        while left and right:
            if left.val <= right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            curr = curr.next

        # 若有剩餘節點  合併到鏈表尾部  在merge sort  中  只會有一個子鏈表會有剩餘節點
        if left:
            curr.next = left
        if right:
            curr.next = right

        return dummy.next
