# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        """

          compare: root.left, subtree
          compare: root.right, subtree

          - check of the rootNode and rootSubtree has same value
          - check of one does not exist

          - check of left has sub tree
          - check if left has subtree left
          - check of 


        """

        def sameTree(p, q):

          if (not p and q) or (not q and p):
               return False

          if not p and not q:
               return True

          if p.val != q.val:
               return False

          left = sameTree(p.left, q.left)
          right = sameTree(p.right, q.right)

          return left and right

     
        def dfs(p, q):

            if not q: return True
            if not p: return False

            if sameTree(p, q):
               return True

            left = dfs(p.left, q)
            right = dfs(p.right, q)

            return left or right

        
        return dfs(root, subRoot)