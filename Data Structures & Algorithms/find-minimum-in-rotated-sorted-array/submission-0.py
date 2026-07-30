class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        [3, 4, 5, 1, 2]
                  l  r

         mid: 5

         if mid > last element
            l = mid + 1
        
        if mid < last element
         r = mid - 1

        [11,13,15,17]
         l  r


        [1,2,3,4,5] 



        [3, 4, 5, 1, 2]
        l = 0
        r = 5

        [3,1,2]
         
         l = 1
         r = 1

         mid = 0
         3 > 1
        """

        l = 0
        r = len(nums) - 1
        
        while l < r:

            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        return nums[l]