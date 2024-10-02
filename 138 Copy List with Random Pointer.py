"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
            
        original_ptr = head
        while original_ptr is not None:
            original_ptr.next = Node(original_ptr.val, original_ptr.next)   # make new nodes and interweave
            original_ptr = original_ptr.next.next   # next node in original list

        original_ptr = head
        new_head = head.next

        while original_ptr is not None:
            if original_ptr.random is not None:
                original_ptr.next.random = original_ptr.random.next      # set random field of the new list
            old_next = original_ptr.next.next   # next node in old list
            # if old_next:
            #     original_ptr.next.next = old_next.next
            # else:
            #     original_ptr.next.next = None
            # original_ptr.next = old_next
            original_ptr = old_next

        old_head = head
        new_head = head.next
        curr_old = old_head
        curr_new = new_head
        
        while curr_old:
            curr_old.next = curr_old.next.next
            curr_new.next = curr_new.next.next if curr_new.next else None
            curr_old = curr_old.next
            curr_new = curr_new.next

        return new_head