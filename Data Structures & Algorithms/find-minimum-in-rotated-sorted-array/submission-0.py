class Solution:
    def findMin(self, nums: List[int]) -> int:
        # rotated means last element is moved from the end to the begining (for one rotation)
        #number of times rotated is the amount of elements taken from the end and put in the begining
        #if number of times rotated is the same as the length of the array then no changes to array 
        # find the minimum value : using binary search 

        # binary search : while left is smaller than right pointer 
        # mid updated as right+left // 2 
        left= 0 
        right= len(nums)-1
        res = nums[0]
        while left<= right:
            if nums[left]< nums[right]:
                res = min(res,nums[left])
                break 
            mid = (right+left)//2
            res = min(res,nums[mid])
            if nums[mid] >= nums[left]:
                left = mid +1
            else:
                right= mid-1 

        return res

        