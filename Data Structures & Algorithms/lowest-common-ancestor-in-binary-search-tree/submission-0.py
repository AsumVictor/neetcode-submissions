# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
          """
          BST:
          Input: root = [5,3,8,1,4,7,9,null,2], p = 3, q = 8

          Output: 5

          root: root > p and q: search right for ancestor

          root: root < p and q: search left for ancestor

          root: root <= p but >= p: root and ancestor


          based: 

          if root < p and q:
                search left of the root
          if root > p and q
               search right

          if root > q and < p or root < q and > p:
               ancestor
          
          if root == p or === q


          """

          def common_ancestor(root, p, q):
              
              if not root:
                return None  # Base case when root is None

              if root.val > p.val and root.val > q.val:
                return common_ancestor(root.left, p, q)  # Search left subtree
              elif root.val < p.val and root.val < q.val:
                return common_ancestor(root.right, p, q)  # Search right subtree
              else:
                return root  # This is the LCA
          
          return common_ancestor(root, p, q)

