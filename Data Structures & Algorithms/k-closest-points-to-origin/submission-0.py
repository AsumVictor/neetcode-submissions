import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        We need the top k distace

        used heap to store the points and thier distace from the origin, 
        but the distance will be the kep

        push all them to the heap with 

        max_heap
        heapify: nlogn

        pop k times. logK
        and store them.

        TC: nlog(n + k)

        [[0,2],[2,0],[2,2]], k = 2
                 ^

           [2, [0,2]
             / \
        [3, [2,0]]  [4, [2,2]]
        
        """
        # helper function to compute distance
        def get_distance(x2, y2):
            x1 = 0
            y1 = 0
            return ((x1 - x2)**2 + (y1 - y2)**2)**(0.5)
        # heapify
        new_points = []
        for point in points:
            # calculate the disatance
            dist = get_distance(point[0], point[1])
            # add to heap
            heapq.heappush(new_points, (dist, point))
        
        # get the closest to the orgin
        res = []
        for _ in range(k):
            dist, point = heapq.heappop(new_points)
            res.append(point)

        # 
        return res



