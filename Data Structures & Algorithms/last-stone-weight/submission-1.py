class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        [2,3,6,2,4]

        sorted
        [2,2,3,4,6]

        What do I need:
         I alway need the top 2  6
            6,4
                  
                   3   
                  / \
                 2   2


        

        """
        import heapq

        # Add all stone to heap
        stones = [-1 * stone for stone in stones]
        heapq.heapify(stones)

        # check if at least stone has one stone, we keep the operation
        while len(stones) > 1:

            # get the top two heavy stones
            heavy_stone_one = heapq.heappop(stones)
            heavy_stone_two = heapq.heappop(stones)

            diff = abs(heavy_stone_one - heavy_stone_two)
            if diff > 0:
                heapq.heappush(stones, -1 * diff)
        

        if len(stones) > 0:
            return -1 * heapq.heappop(stones)
        else:
            return 0



