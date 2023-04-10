/** 
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
const addTwoNumbers = function(l1, l2) {
    //創立鏈結
    let result = new ListNode(0);
    // 此用於指針移動
    let head = result;
    //進位
    let carry = 0;
    
    while(l1 !== null || l2 !== null || carry !== 0){
        //加總
        let sum = 0;
        //不為null時  將值加至加總並移動至next
        if(l1 !== null){
            sum += l1.val;
            l1 = l1.next;
        }
        //不為null時  將值加至加總並移動至next
        if(l2 !== null){
            sum += l2.val;
            l2 = l2.next;
        }
        //加總將上進位的值  為0 or 1
        sum += carry;
        
        //sum >= 10 時  取餘數 並進位  <10 進位為0
        if(sum >= 10) {
            sum = sum % 10;
            carry = 1;
        } else {
            carry = 0;
        }
        //創建新listNode並移動指針
        head.next = new ListNode(sum);
        head = head.next;
    }
    //最後回傳next  頭的值為0    
    return result.next;
};