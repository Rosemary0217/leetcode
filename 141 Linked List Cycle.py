# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# use a hash map, but this is unefficient
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        vis = list()
        tmp = head
        while tmp.next is not None:
            if tmp not in vis:
                vis.append(tmp)
                tmp = tmp.next
            else:
                return True
        return False
    

# use fast and slow pointers
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        slow, fast = head, head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False