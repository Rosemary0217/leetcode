# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# class Solution:
#     def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
#         """
#             Reverse by values instead of position 
#         """
#         def reverseList(node, end):   # reverse the list in a recursive manner
#             if node.next == end:
#                 return node
#             new_head = reverseList(node.next, end)
#             node.next.next = node
#             node.next = None
#             return new_head

#         santinel = ListNode(val=-1,next=head)
#         head_this_group = head
#         head_next_group = head
#         node_b4_this_group = santinel

#         ptr = head
#         while ptr:
#             if ptr.val % k == 0:
#                 head_this_group = head_next_group
#                 head_next_group = ptr.next
#                 node_b4_this_group.next = reverseList(head_this_group, head_next_group)
#                 head_this_group.next = head_next_group
#                 node_b4_this_group = head_this_group
#             ptr = ptr.next

#         return santinel.next
        
import typing

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head, k):
        def reverseList(node, end):   # reverse the list in a recursive manner
            if node.next == end:
                return node
            new_head = reverseList(node.next, end)
            node.next.next = node
            node.next = None
            return new_head

        santinel = ListNode(val=-1,next=head)
        head_this_group = head
        head_next_group = head
        node_b4_this_group = santinel

        ptr = head
        cnt = 0
        while ptr:
            cnt += 1
            if cnt % k == 0:
                head_this_group = head_next_group
                head_next_group = ptr.next
                print('reverse from {} to {}'.format(head_this_group.val, head_next_group.val-1))
                node_b4_this_group.next = reverseList(head_this_group, head_next_group)
                head_this_group.next = head_next_group
                node_b4_this_group = head_this_group
                ptr = head_this_group
            ptr = ptr.next
            
        return santinel.next
    
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

soln = Solution()
head = soln.reverseKGroup(node1, 2)
while head:
    print(head.val)
    head = head.next