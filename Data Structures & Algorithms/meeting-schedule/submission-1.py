"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # return bool 
        # input: list of pairs( in a tuple)
        # end time of pair i<= start time of pair  i+1 
            # works if its sorted
        #[(9,15),(5,8)]
        if not intervals:
            return True
        intervals.sort(key=lambda x: x.start)
        for i in range (len(intervals)-1):
            if intervals[i].end > intervals[i+1].start:
                return False
        return True 

        

