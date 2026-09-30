"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # determine if any meetings are overlapping 
        #sort meeting times by end dates
        # compare if the start of the next meeting is before the end of the current meeting
        intervals.sort(key=lambda x :x.end )
        for i in range(1,len(intervals)):
            i1= intervals[i-1]
            i2= intervals[i]
            if (i2.start<i1.end):
                return False
        return True



        
