# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
#解法1  使用快慢指針  慢指針一次走一步  快指針一次走兩步  當快指針走道末或超過時 此時慢指針指向的就是中間節點
def middleNode(head: ListNode) -> ListNode:
    slow, fast = head, head
    #可能越界  會導致fast.next is None  and None.next will throw exception
    try:
        while fast.next:
            slow = slow.next
            fast = fast.next.next
    except:
        return slow
    return slow