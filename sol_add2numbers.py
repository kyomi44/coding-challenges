# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = False
        
        ans2 = ListNode()
        ans = ans2
        
        while l1 or l2:
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0
            total = l1Val + l2Val
            
            if carry:
                total +=1
            
            carry = True if total >= 10 else False
            
            ans.next = ListNode(total % 10)
            
            ans = ans.next
            
            if l1:l1 = l1.next
            if l2:l2 = l2.next
                
        if carry == True:
            ans.next = ListNode(1)
            
        return ans2.next