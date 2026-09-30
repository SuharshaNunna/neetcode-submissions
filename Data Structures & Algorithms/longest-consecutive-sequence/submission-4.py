class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # brute, sort array (O(n*logn)), then add to consecutive count if differnece between curr and next is 1  (O(n))
        res = 1
        nums.sort()
        if not nums:
            return 0
        maxres=1
        for i in range (len(nums)-1):
            if (nums[i+1]==nums[i]):
                continue
            elif ((nums[i+1]-nums[i]) == 1):
                res +=1
                maxres= max(maxres,res)
            else:
                res = 1 
        return maxres 
 
        