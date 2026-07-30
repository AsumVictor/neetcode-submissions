class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        - Find the minimum steps to reach n
        - for each step, I need the maximum step that reach the end goal
        - for each step, I could jump from 1...nums[i]

        pick from nums[i] ..1
        Pick the hihest jump at each step

        [2,2,0,1]
             ^
        
        i within bound of maxJump

        min_jumps: 2
         1..3
        [2,4,1,1,1,1, 7]
        
               ^
                    ^
        """


        res = 0

        l = r = 0

        # until we reach the last index
        while r < len(nums) - 1:

            # check the farthest can we can
            farthest = 0

            # we go throuh all the possible jumps and pick the far
            # range 3,4
            # i + 1, i + nums[i] + 1
            for i in range(l, r + 1):

                farthest = max(farthest, nums[i] + i)

            
            # set left to right + 1
            l = r + 1
            r = farthest
            res += 1

        return res


