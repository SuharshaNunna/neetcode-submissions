class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
# find the largetst sub array and return the largest sum 
# sub array: continous squence of elements 
#can add an element to a array and store its sum is the max of maxs ( only stores if it beats current max )
# this is dp approach ^
        #dp = [*nums]
    #copys nums to dp 
        #for i in range(1, len(nums)):
            #dp[i] = max(nums[i], nums[i]+dp[i-1])
        # updates the index with the max subarray  leadning up to it
        #return (max(dp))

# add elements, and store max of max , if added element makes sum - then reset sum to 0  
# ^ this is greedy approach  

        maxsum, currsum= nums[0], 0 
        for n in nums:
            if currsum < 0:
                currsum=0
            currsum+=n
            maxsum= max(maxsum,currsum)
        return maxsum