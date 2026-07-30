# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """

        loop theough by level by level

        for each level I will append values

        for each level:

          - loop through the queue and collect all values while deleting them
          - collect all children and assign to the quee

        """

        queue = [root]
        result = []
        
        if not root:
          return []

        while queue:
          nextLevel = []
          levelChildren = []
          for node in queue:
               if node.left:
                    nextLevel.append(node.left)

               if node.right:
                    nextLevel.append(node.right)

               levelChildren.append(node.val)

          result.append(levelChildren)
          queue = nextLevel


        return result


