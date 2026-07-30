class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        [1,2,3]
        ^
        []
        Find subset of set posible subset

        * any combination of this without repeatition
        []

        base case:
        when: i >= len(s): we have explore all path

        list of choice:
         either choice the current element or not

         prunning
         *  

         []
         / \
     [1]   []





        """

        solution = []

        def backtrack(path, i):

            # base case
            if i == len(nums):
                solution.append(path.copy())
                return

            # chioce
            # exclude
            backtrack(path, i + 1)

            # include
            # modify state
            path.append(nums[i])
            # recurse
            backtrack(path, i + 1)
            # undo
            path.pop()

            return

        
        backtrack([], 0)       

        return solution
