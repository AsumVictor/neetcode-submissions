class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
         0 1 2 3 4
        [1,2,3,2,2]

        slow = 0
        fast = 0
        next_slow = nums[slow] mod len
        fast = nums[fast]
        fast = nums[fast]

        if slow == fast
        """

        n = len(nums)
        slow = 0
        fast = 0
        slow = nums[slow]
        fast = nums[fast]
        fast = nums[fast]

        while nums[fast] != nums[slow]:

            slow = nums[slow]
            fast = nums[fast]
            fast = nums[fast]

        fast = 0
        while nums[fast] != nums[slow]:

            slow = nums[slow]
            fast = nums[fast]

        return nums[fast]
