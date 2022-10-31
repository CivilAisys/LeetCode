/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
//解法1
const swapPairs = function(head) {
    
    //若是head === null or head.next === null  就可直接回傳;
    if(head === null || head.next === null) return head;

    //用number紀錄當前loop到第幾個節點
    let number = 1;
    //紀錄head是哪一個node
    let header = head;
    //紀錄當前loop到的節點  起點為head
    let currentNode = head;
    //紀錄loop時的前一個節點
    let previousNode = null;

};

function ListNode(val, next) {
    this.val = (val === undefined ? 0 : val)
    this.next = (next === undefined ? null : next)
}

//swapPairs( new ListNode(1,new ListNode(2,new ListNode(3, new ListNode(4, undefined)))))