class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        heights = [7,1,7,2,2,4,13,14]
                                   ^
                [(0, 1), (2,2), (4,2), (5,4), (6, 13)]

                max_area = 7

                if smaller than top:
                    calculate the area and pop()
                    use the pop value to be the index of the curr bar

                   when meet bigger element: add it and conclus
        Output: 8
        [7,1,7,2,2,4]
        (0,1), (2,2), (4,2), (5, 4)

        5

        7
        """
        stack = [] # (index, height)
        max_area = 0
        for i, height in enumerate(heights):
            j = i
            while stack and stack[-1][1] > height:
                index, h = stack.pop()
                max_area = max(max_area, (i - index) * h)
                j = index
            
            stack.append((j, height))

        
        last_index = stack[-1][0]
        for i, h in stack:

            max_area = max(max_area, (len(heights) - i) * h)

        
        return max_area





