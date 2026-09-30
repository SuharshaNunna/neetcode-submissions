class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
# merge the intervals and return merged + untouched intervals
# sort the intervals by the start day , then if the first end is more than next start = merge 

        #sort list of pairs , i stands for interval , sorting by start means i[0] ... i[1] would be end  
        intervals.sort(key=lambda i :i[0])
       #initializing intervals 
        output = [intervals[0]]
        for s,e in intervals[1:]:
            #end value of most recent interval 
            lasti=output[-1][1]
            if lasti>= s: 
                # merge, keep last start , change last end to new end 
                output[-1][1]=max(lasti,e)
            else:
                output.append([s,e])
        return output

            