class Solution:
    def rob(self, nums: List[int]) -> int:
        # 1- n
        # money from house to house
        """
        1 2 3 4 5 6
        ^...^...^
        1..2..3
        each house choose to rob or not
        1, 2

        func i:

            if 
        
        backtrack:
          2 - jump 8
        
         search i:
         i < n:
           return 0

         rob this house:
         not rob (i + 1)
         


        """

        N = len(nums)
        if N <= 2:
            return max(nums)
        
        memo = {}
        def solve(i):
            # cases
            if i >= N:
                return 0

            if i in memo:
                return memo[i]
            
            # choose this number
            skip = solve(i + 1)
            rob = nums[i] + solve(i + 2)
            memo[i] = max(skip, rob)
            return memo[i]

        return solve(0)










