class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float("-inf")
        runningSum = float("-inf")
        
        for n in nums:
            runningSum = max(n, runningSum + n)
            res = max(runningSum, res)

        return res
