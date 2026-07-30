# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
       """
        number of nodes from left 
        diff(left, right) = 1,0,-1 : balance

        count left and right
       """



       def dfs(node, height):

            if not node:
                return [True, height]

            
            bol_l, left = dfs(node.left, 0)
            bol_r, right = dfs(node.right, 0)


            return [(abs(left - right) <= 1) and bol_l and bol_r,max(right , left) + 1]
            

       return dfs(root, 0)[0]

