import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        [2,3,1,5,4], k = 2
        Naive: sort() nlogn

        heapify: in max_heap

        I wil pop k time and return the result of the last pop


        """

        # invert number to negative to use min heap
        nums = [-1 * n for n in nums]
        # heapify nums
        heapq.heapify(nums)

        # pop the heap k times and return the last pop
        res = None
        for _ in range(k):
            # pop from the heap and assign to res
            res  = -1 * heapq.heappop(nums)
        
        return res
