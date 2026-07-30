import heapq

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        """

        * feasibility : dont need actual groups
        * boolean feedback
        * values are consietndly increase by one
         
         max-2
        [1,2,3,3,4,5,6,7]
        2

        1: 0
        2: 0
        3: 0
        4: 2
        5: 1

        while the heap:

            min = 2

            for 2 to 5:
              count i == 0 ot not as key:
                return
              
            
            1122334455
             ^
              ^
            1:1
            2:1
            3:2
            4:2
            5:2
            1 == 1:
              
               
             

                          [2]   1
                        [3,4]
                      [5,6,7]
                      []
                      []






        """

        # check if the bucket is enough to group
        n = len(hand)

        if n % groupSize !=0:
            return False

        
        # keep frequency
        counter = {}
        for h in hand:
            counter[h] = 1 + counter.get(h, 0)
        
        # heap
        heap = list(counter.keys())
        heapq.heapify(heap)

        # lets form while heap 
        while heap:

            first  = heap[0]

            for h in range(first, first + groupSize):

                # check if this exist
                if h not in counter:
                    return False

                counter[h] = counter[h] - 1

                if counter[h] == 0:
                    # check if the minimum
                    if h != heap[0]:
                        return False
                    
                    heapq.heappop(heap)
        
        return True

