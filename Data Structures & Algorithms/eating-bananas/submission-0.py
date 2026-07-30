class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        _ _ _
        8 hours
        bana / hour = speed = k

        [3,6,7,11]
         ^
         1b/hr

         n = 1 hr
         3 = ?

         b[i] / n : floor division

        1 - 11
        NNNNNNNEEEEEE
        """

        def can_eat(k):

            total_hrs = 0
            for i in range(len(piles)):

                hr = 0
                if piles[i] % k == 0:
                     hr = piles[i] / k
                else:
                    hr = (piles[i] // k) + 1

                total_hrs += hr
                if total_hrs > h:
                    return False
                
            return True

        max_bph = max(piles)
        min_bph = 1 
        

        min_index = -1
        while min_bph <= max_bph:
            mid = (max_bph + min_bph) // 2

            if can_eat(mid):
                min_index = mid
                max_bph = mid - 1
            else:
                min_bph = mid + 1

        
        
        return min_index