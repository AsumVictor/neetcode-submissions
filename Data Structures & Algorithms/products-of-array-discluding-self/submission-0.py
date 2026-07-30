class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1;
        result = []
        result.append(prefix)	
               
        for i in range(len(nums) -  1):
            prefix = prefix * nums[i]
		
            result.append(prefix) 
	
        postfix = 1;
        result[-1] = result[-1] * postfix
        for i in range(len(nums) - 1, 0, -1):
            postfix = postfix  * nums[i];
            result[i - 1] = result[i - 1] * postfix
	
        return result
