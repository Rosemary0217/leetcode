# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:  
        '''
            In-place merge in tmp1
        '''
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        tmp1 = list1 if list1.val <= list2.val else list2  # tmp1 points to the list with smaller header value
        tmp2 = list2 if tmp1 == list1 else list1
        cursor = tmp1
        while cursor is not None and tmp2 is not None:
            while cursor.next is not None and cursor.next.val <= tmp2.val:
                cursor = cursor.next    # cursor points to the last node smaller than tmp2.val  
            tmp = cursor.next
            cursor.next = tmp2
            tmp2 = tmp2.next
            cursor.next.next = tmp
            
        return tmp1