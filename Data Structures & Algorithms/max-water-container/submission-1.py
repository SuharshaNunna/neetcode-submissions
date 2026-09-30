class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # amount of water =  distance between bins * height of lowest bin 
        # to maximize need greatest distance (i) and greatest hight (value)
        # brute force: calculate all potential areas(O(n^2)) and return max
        # two pointers have one at 0 and one at n-1 
        # calc area 
        # if next height > last max height+ ( differnce of i) incriment counter
        size = len(heights) 
        rindx, lindx, = size-1, 0 
        sol=0
        #starting from first index 
        while lindx<rindx:
            water=(min(heights[rindx],heights[lindx]))* (rindx-lindx)
            sol= max(water,sol)
            if (heights[rindx]>heights[lindx]):
                lindx+=1
            else:
                rindx-=1             
        return sol
