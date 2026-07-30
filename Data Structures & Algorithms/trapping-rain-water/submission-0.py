class Solution:
    def trap(self, height: List[int]) -> int:
        """
        [0,2,0,3,1,0,1,3,2,1]

        [0,0,2,0,2,3,2,0,0,0]
        

        max: 3

        """

        res = [0] * (len(height))
        max_h = 0

        for i in range(len(height)):
            max_h = max(max_h, height[i])
            res[i] = max_h

        total_water = 0
        max_h = 0
        for i in range(len(height) - 1, -1, -1):
            max_h = max(max_h, height[i])
            left_max = res[i]
            amount_of_water = min(max_h, left_max) - height[i]
            total_water += amount_of_water
        
        return total_water




        