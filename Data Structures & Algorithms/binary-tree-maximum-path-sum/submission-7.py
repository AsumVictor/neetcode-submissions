# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        """
        for every node. 
        Consider:
          - maxPath from top only, 
          - maxpath + curr Value 
          - max_sum from left, 
          - max_sum from right only
          - sum of left + right + curr node


          max: -5
          left: 10

          20:
           -max: -15
            curr: 20


           15: 
           max: 20
             - 20, 20+15, 15
                 = 35
                
            
            -5:
              max: 35
                -5, -5 + 35, 35
                  = 35
             35

        -15, -inf
            l: 10, -inf
                   l: null, -inf
                result_l =   -inf
                   r: null, -inf
                result_r =   -inf
              10 = max("-inf", "-inf", 10, "-inf")
            l_result = 10

            r

               

            1
             \
               2
            
            l = -inf

            1
           / \
        -2    3
            



                  


        """
        res = float("-inf")
        def getMaxValue(node):
            nonlocal res
            # if node does not exist resutn 0
            if not node: 
                return float("-inf")

            # get the max_sum from the left
            maxLeftSum = getMaxValue(node.left)

            # get max sum from the right
            maxRightSum = getMaxValue(node.right)

            # compute the path from both path
                         # max of indidual
            res = max(res, maxLeftSum + node.val, maxRightSum + node.val, node.val, maxRightSum + maxLeftSum + node.val)

            maxSum = max(
                        maxLeftSum + node.val, 
                        maxRightSum + node.val, 
                        node.val
                        )

            return maxSum
                        

          
        
        getMaxValue(root)
        return res


             