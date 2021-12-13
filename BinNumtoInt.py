# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        
        powa = []
        count = 0
        prevcount = 0
        ans = 0
        
        while head:
            if head.val:
                dis = count - prevcount
                prevcount = count
                powa.append(dis)
            
            count += 1
            head = head.next
        
        print(powa)
        print(count)
        
        while powa:
            count -= powa[0]
            ans += 1 * 2**(count-1)
            powa.pop(0)
            
        return ans
            