# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# 使用快慢指針 快指針先走n步 接著快慢一起走直到快指針到尾部  此時慢指針所指就是要刪除的節點
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # dummy head
        dummy = ListNode(0, head)
        # 快慢指針
        first, second = dummy, dummy

        # 快指針先走n步
        for i in range(n):
            first = first.next
        # 快慢一起走  直到快指針抵達尾部
        while first.next is not None:
            first = first.next
            second = second.next
        # 刪除second所指向節點 因為原慢指針指向為dummy head  故實際要刪除的是second.next
        second.next = second.next.next

        return dummy.next
