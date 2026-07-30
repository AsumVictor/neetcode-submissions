# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
          """
          2    
            \
              3  

           2    
            \
              4  

          """

          def hasSameVal(p, q):

               if (p and not q) or (not p and q):
                    return False

               if not p and not q:
                    return True

               
               if p.val != q.val:
                    return False

               
               left = hasSameVal(p.left, q.left)
               right = hasSameVal(p.right, q.right)

               return (left and right)

          
          return hasSameVal(p, q)


        

