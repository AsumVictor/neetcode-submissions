# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """

        for every node:

            if left node exist:
                then the side will be the left node
            else:
                right

            


        """

        queue = [root]
        if not root:
            return []

        result = []
       
        while queue:

            next_successor = []

            for n in queue:

                if n.left:
                    next_successor.append(n.left)
                
                if n.right:
                    next_successor.append(n.right)
            
            result.append(queue[-1].val)
            queue = next_successor

        return result


        