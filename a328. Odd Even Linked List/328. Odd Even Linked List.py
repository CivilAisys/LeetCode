# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# 解法1 遍歷鏈表將奇數節點及偶數節點分別串在一起
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        odd, even = head, head.next  # 定義兩指針  指向奇數及偶數的頭部
        even_head = even  # 保存偶數的頭部　以便後面串接在奇數尾部

        #  遍歷鏈表並將奇數偶數分別做串接
        while even and even.next:
            odd.next = even.next  # 奇數串接
            odd = odd.next  # 奇數向後移一格
            even.next = odd.next  # 偶數串接
            even = even.next  # 偶數向後移一格
        # 將偶數鏈表串接再奇數鏈表後
        odd.next = even_head
        return head
