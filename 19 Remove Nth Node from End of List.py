#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        list=[]
        p=head
        while p:
            list.append(p)
            p=p.next
        if n==len(list):
            if n==1:
                return None
            else:
                return list[1]
        else:
            list[-(n+1)].next=list[-n].next
        return head
        