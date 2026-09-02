class Solution:
    def climbStairs(self, n: int) -> int:
        # start with 2 or 1
        # for each you choose 1 or 2
        # if curr > n: you ignore
        # xurr == n means weve reach

        # 0  1  2  3  4  5  6
        # 0  1

        # 0 - 0
        # 1 - 1
        # 2 - 2 (1.1 2)
        # 3 - (1.1.1 2.1 1.2)
        # 4 - (1.1.1.1 1.1.2 1.2.1 2.1.1 2.2)
        # 4 - 3, 2... 3

        memo = {}
        def number_of(n):
            #
            if n == 0:
                return 0
            
            if n == 1:
                return 1
            
            if n == 2:
                return 2
            
            if n in memo:
                return memo[n]
            
            result = number_of(n - 1) + number_of(n - 2)
            memo[n] = result
            return memo[n]

        
        return number_of(n)

        # def move_step(curr):

        #     # check
        #     if curr == n:
        #         return 1
            
        #     if curr > n:
        #         return 0

            
        #     # add one
        #     one_moves = move_step(curr + 1)
        #     two_moves = move_step(curr + 2)

        #     return one_moves + two_moves
        
        # return (move_step(0))


