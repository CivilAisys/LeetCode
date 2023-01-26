class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
#解法1  使用迴圈遍歷ListNode  並將遍歷到的節點都放到頭
def reverseList(head: ListNode) -> ListNode:
    #因為遍歷時head會移動  故建立new_head new_head.next指向當前head
    new_head = ListNode()

    while head:
        next = head.next
        head.next = new_head.next
        #更新新的頭部  並將head移向下一個要移至頭部的節點
        new_head.next = head
        head = next

    return new_head.next

