'''
want non overlapping 
sort 
check if end time is before or = next start time 
- if no 
        overlap detected 
        count +1
        remmvoe i+1 
- yes 
    keep iterating 
[[1,2],[1,3],[2,3],[3,4]]
'''
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda pair: pair[1])
        prevEnd = intervals[0][1]
        res = 0
        for i in range(1, len(intervals)):
            if prevEnd > intervals[i][0]:
                res += 1
            else:
                prevEnd = intervals[i][1]
        return res