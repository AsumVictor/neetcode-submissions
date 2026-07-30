class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Input: temperatures = [30,38,30,36,35,40,40]
                                              ^

        [40,36]
        [0,0, 1,2]
        Output: [1,4,1,2,1,0,0]

        warmer means: tem[i ++] > tem[i]

        TC: O(n2)

        pop when greater or equal
        """
        stack = []
        result = []
        for i in range(len(temperatures)-1, -1, -1):

            if stack:
                
                while stack and temperatures[i] >= temperatures[stack[-1]]:
                    stack.pop()

                if not stack:
                    result = [0] + result
                else:
                    result = [stack[-1] - i] + result

            else:
                result = [0] + result

            stack.append(i)

        
        return result

        
        