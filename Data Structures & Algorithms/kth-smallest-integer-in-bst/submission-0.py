# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        node

        go to left:
        if no node return k + 1

        go to left:
            check if has found

        """
        self.res = None
        def dfs(node, val):

            if not node:
                return (val + 1, False)

            l_val, found = dfs(node.left, val)
            if found:
                return (l_val + 1, found)
            
            if l_val == k:
                self.res = node
                return (l_val + 1, True)
            
            r_val, found = dfs(node.right, l_val)

            return (r_val, found)

        dfs(root, 0)
        return self.res.val



        