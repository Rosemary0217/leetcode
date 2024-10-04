# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        tmp_head = head
        tmp_end = head

        def reverseList(node):   # reverse the list in a recursive manner
            if node.next == tmp_end:
                return node
            new_head = reverseList(node.next)
            node.next.next = node
            node.next = None
            return new_head

        if left > 1:   # if 'left' is not the first node, find the node before it
            for i in range(left - 2):
                tmp_head = tmp_head.next
                tmp_end = tmp_end.next

            node_b4_left = tmp_head
            tmp_head = tmp_head.next
            
            for i in range(right - left + 1):   # tmp_end is the node next to 'right'
                tmp_end = tmp_end.next  
            if tmp_end:
                tmp_end = tmp_end.next
            node_b4_left.next = reverseList(tmp_head)
        else:   # if 'left' is the first node, then no need to reconnect on the left
            for i in range(right):
                tmp_end = tmp_end.next
            head = reverseList(tmp_head)     # head is now 'right'
        tmp_head.next = tmp_end     # don't forget to reconnect the whole list
        return head

        