import heapq

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        """
        * binary
        * two next values

        [7,1]
        [2,1]
        [3,1]
        

        triplets= 
        [[2,5,6],
        [1,4,4],
        [5,7,5]]
         
         [5,2,1] = 5
         [4] = 
         [6, 5, 4] = 

      [2,5,3],[1,7,5]

      [2,7,5]

      []
      []
      []





        """

        # sort
        heapa = []
        heapb = []
        heapc = []
        ta, tb, tc = target

        for x, y, z in triplets:
            if x <= ta and y <= tb and z <= tc:
                heapq.heappush(heapa, -1 *x)
                heapq.heappush(heapb, -1 *y)
                heapq.heappush(heapc, -1 *z)
        
        while heapa and -1 *heapa[0] > ta:
            heapq.heappop(heapa)
        
        while heapb and -1 * heapb[0] > tb:
            heapq.heappop(heapb)

        while heapc and -1 * heapc[0] > tc:
            heapq.heappop(heapc)

        if not (heapa and heapb and heapc):
            return False

        
        a, b, c = -1 * heapa[0], -1 *heapb[0], -1 *heapc[0]

        return a == ta and b==tb and c==tc
        



