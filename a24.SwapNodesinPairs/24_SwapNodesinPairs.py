class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
#解法1
def swapPairs(head: ListNode) -> ListNode:
    #若head == None  or head.next == None   return head
    if head == None or head.next == None:
        return head
    
    #將head前套上node
    fakeNode = ListNode()
    fakeNode.next = head
    #保存fakeNode地址
    result = fakeNode

    #需要檢查下個及下下個皆有值時才進行調換
    while fakeNode.next != None and fakeNode.next.next != None:
        #先保存下個及下下個的位址
        a = fakeNode.next
        b = fakeNode.next.next

        #改變fakeNode.next為b 0 -> 2
        fakeNode.next = b
        #改變 下個.next = b.next 0 -> 2 -> 1 -> 3
        a.next = b.next
        #改變下下個.next = a  0 -> 2 -> 1
        b.next = a
        #移動fakeNode指針至第二個 0 -> 2 -> 1(指針位置) -> 3
        fakeNode = a

    return result.next


swapPairs(ListNode(1, ListNode(2)))

        
    