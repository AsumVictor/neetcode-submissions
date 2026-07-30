"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

|--0-------30
|--0---10  prev

start < end of curr

"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda x: x.start)
        if not intervals:
            return True
        prev = intervals[0]

        for i in range(1, len(intervals)):
            curr = intervals[i]
            if curr.start < prev.end:
                return False

            prev = curr
        
        return True


            