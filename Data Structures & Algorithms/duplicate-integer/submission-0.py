class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         original = set(nums)
         return len(original) != len(nums)