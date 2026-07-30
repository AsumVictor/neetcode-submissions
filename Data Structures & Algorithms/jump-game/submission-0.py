class Solution:
    def canJump(self, nums: List[int]) -> bool:

        lastTarget = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            # check the jump from current
            currJump = i + nums[i]

            # check if current jump can reach target
            if currJump >= lastTarget:
            
                lastTarget = i

        return lastTarget == 0
        