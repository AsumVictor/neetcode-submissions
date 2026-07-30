class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        
        [1,7,2,5,4,7,3,6]
         0 1 2 3 4 5 6 7
         i
                        j

        h = min of ith and jth position of height
        width = j - i
        7
        if cuu water > prevSum: update
        if ith < jth: increase i
        else with increse j

        [1,7,2,5,12,3,500,500,7,8,4,7,3,6]
        max_area = 0
        lt = 0
        rt = 13
        """

        max_area = 0
        lt = 0
        rt = len(heights) - 1

        while lt < rt:
            h = min(heights[lt], heights[rt])
            w = rt - lt

            if h * w > max_area:
                max_area = h * w

            if heights[lt] < heights[rt]:
                lt += 1
            else:
                rt -= 1

        return max_area

