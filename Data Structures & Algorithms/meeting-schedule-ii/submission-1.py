"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

* Sort based on start time
|--0----------------------------------------40-|  
     |-5---10| 
                 |-15--------20-|            40  -- 45

n = 1

[15,20]
[5,10]
days = 2
n = 3

days = 1

prevEnd = 40
 day = 1
for each of interval
 if curr start time < prev end time 
    move to next day
    set prev to curr time
end = 1320
n = 1
end: 1358
intervals=[(685,1353),]
(218,918)
day = 2
"""
from collections import deque

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # sorting based on start time
        intervals.sort(key=lambda x: x.start)
        queue = deque(intervals)
        days = 0
       
        while queue:

            # get last from queue:
            days += 1
            curr = queue.popleft()
            n = len(queue)
            end = curr.end
            for _ in range(n):
                new = queue.popleft()
                if new.start < end:
                    queue.append(new)
                else:
                    end = new.end
                
        
        return days

                



