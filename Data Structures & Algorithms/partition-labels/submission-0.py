import heapq
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """

        as many mean taking a single character into new bughest

        "x y x x y z b z b b i s l x"
         ^                  ^

         met new:
          add to buck if it has not
        if meet at same sequence: if char in same substring
         set the bug:
           running = 1 

         running = 1
         buckget: 
         {x,y}


        for every char:

        pick smallest length withour repeation as possible

        x y x x y z b z b b  i   s  l
        0 1 2 3 4 5 6 7 8 9  10 11  12
        |-----
           -----|
                  |---|
                    |-----|
                             |  |   |    

     min(start), max(end)            

        

       


        [(1, 4), (5, 7), (6, 9), (10, 10), (11, 11), (12, 12)]
        (0, 3), 

        """

        interval = {}
        for i, char in enumerate(s):
            
            if char in interval:
                start, end = interval[char]
                interval[char] = (min(start, i), max(end, i))
            else:
                interval[char] = (i, i)

        
        # use heap
        heap= list(interval.values())
        heapq.heapify(heap)
        print(heap)

        result = []
        while heap:
            
            # get smallest
            start, end = heapq.heappop(heap)

            # check conflict interval
            if heap and end >= heap[0][0]:
                # merge and put it back
                start2, end2 = heapq.heappop(heap)
                start = min(start, start2)
                end = max(end, end2)

                # pop and add the new one
                heapq.heappush(heap, (start, end))
            else:
                # calculate the lend and add
                result.append(end - start + 1)

        
        return result



        

        

            
        