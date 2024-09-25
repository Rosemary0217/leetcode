# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        res = ListNode((l1.val + l2.val) % 10)
        carry = (l1.val + l2.val) // 10
        tmp3 = res
        tmp1 = l1.next
        tmp2 = l2.next
        while tmp1 is not None or tmp2 is not None:
            digit1 = 0 if tmp1 is None else tmp1.val
            digit2 = 0 if tmp2 is None else tmp2.val
            tmp3.next = ListNode((digit1 + digit2 + carry) % 10)
            tmp3 = tmp3.next
            carry = (digit1 + digit2 + carry) // 10    # compute new carry
            tmp1 = tmp1.next if tmp1 is not None else None
            tmp2 = tmp2.next if tmp2 is not None else None
        
        if carry > 0:
            tmp3.next = ListNode(carry)
        return res