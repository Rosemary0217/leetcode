# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
#         if not p and not q:
#             return True
#         if not p or not q:
#             return False
#         res1, res2 = list(), list()
#         def inorder(node, res):
#             if not node:
#                 return res
#             inorder(node.left, res)
#             res.append(node)
#             inorder(node.right, res)
#             return res
#         res1 = inorder(p, res1)
#         res2 = inorder(p, res2)
#         n1, n2 = len(res1), len(res2)
#         if n1 != n2:
#             return False
#         for i in range(n1):
#             if res1[i] != res2[i]:
#                 return False
#         return True
        
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)