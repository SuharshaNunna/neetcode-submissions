class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #only returning product - not array 
        # [1,2,4,-3,5, 9]
        # make decison ( include next number in sub array and update max  or no )
        # keep track of new subaray or no 
        res= max(nums)
        currmin= 1
        currmax=1 
        for n in nums:
            # edge 
            if n == 0:
                currmin= 1
                currmax=1 
                continue 
            temp= currmax*n
            currmax = max(n*currmax, n* currmin, n)
            currmin = min(temp, n* currmin, n)
            res = max(res, currmax)
        return res
# consider - values impact 



# error [-2,3,-4] , 3  is set to curr sum then another neg wouldnt cancel out negative issue 
 

        