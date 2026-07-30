class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        permutation of numbers
         [1,2,3]
         path is permuation of numbers
         base case: when path == n: it mean we have explore all numbers

        choices:
        [1,2,3]      

        2:
        1,3
        1:
        3
        


        [] * 1,2,3 first:

        seconds: all values that is not the current index
        all values in path.


        for all choices: generate choices
        index should not in already seens





        """

        solution = []
        n = len(nums)

        def backtrack(path, seen, i):

            if len(path) == n:
                solution.append(path.copy())
                return
            
            for k in range(n):
                if k not in seen:

                    # choice
                    path.append(nums[k])
                    seen.add(k)

                    backtrack(path, seen, k + 1)

                    # undo choice
                    path.pop()
                    seen.remove(k)
            
            return

        backtrack([], set(), 0)

        return solution



        
        