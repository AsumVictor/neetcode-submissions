class Solution:
    def countBits(self, n: int) -> List[int]:
        
        # naive way to to for each number get the hamming weight

        # but we start from n:
        # get the bit and we turn on and off
        
        # 
        dp = [0] * (n + 1)
        for i in range(1, n + 1):

            # check the dp
            dp[i] = dp[i >> 1] + (i & 1)

            # 
        return dp