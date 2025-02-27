from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def merge_sort(head):
            if not head or not head.next:  # null or only one node
                return head
            fast, slow = head.next, head    # FAST POINTER MUST STARTS FROM THE SECOND NODE!!!
            while fast and fast.next:   # find the middle node using two pointers
                fast = fast.next.next
                slow = slow.next 
            mid = slow.next   # split the linked list
            slow.next = None
            sub1 = merge_sort(head)
            sub2 = merge_sort(mid)
            return ordered_merge(sub1, sub2)

        def ordered_merge(sub1, sub2):
            ptr1, ptr2 = sub1, sub2
            sentinel = ListNode(-1)
            res = sentinel
            while ptr1 and ptr2:
                if ptr1.val <= ptr2.val:
                    res.next = ptr1
                    ptr1 = ptr1.next
                else:
                    res.next = ptr2
                    ptr2 = ptr2.next
                res = res.next

            res.next = ptr2 if not ptr1 else ptr1
            return sentinel.next

        return merge_sort(head)

    
# h = ListNode()
# nums = [4,2,1,3]
# p = h
# for num in nums:
#     p.next = ListNode(num)
#     p = p.next

# sol = Solution()
# print(sol.sortList(h.next))
            