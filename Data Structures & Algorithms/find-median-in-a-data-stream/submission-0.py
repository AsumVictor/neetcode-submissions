class MedianFinder:
    """
    6 1 3 6 9 0 4 2
    [6,1,3] nlogn

    [3,1]     [6,9]
    max   min

    logn

     add to max

    if len max - min > 2:
        pop from max and add to min
    


    median:
      check if len max > len min:
        reutn top of max
      if len min > max
         return top of min
      else:
        return top of mn + top of max / 2
    

    """
    import heapq

    def __init__(self):
        # min heap and max heap
        self.min_heap = []
        self.max_heap = []


    def addNum(self, num: int) -> None:
        # add to max heap
        heapq.heappush(self.max_heap, -1 * num)  #  0(logn)

        # check the top ele
        if self.min_heap and (self.max_heap[0] * -1) > self.min_heap[0]:
            val = -1 * heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)

        
        # we check if the length of the max is greater than min
        if len(self.max_heap) > len(self.min_heap) + 1:
            val = -1 * heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)
        
        # we check if the length of the max is greater than min
        if len(self.min_heap) > len(self.max_heap) + 1:
            val = -1 * heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, val)

    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return self.max_heap[0] * -1
        elif len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        else:
            min_val = self.min_heap[0]
            max_val = self.max_heap[0] * -1
            return (min_val + max_val) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()