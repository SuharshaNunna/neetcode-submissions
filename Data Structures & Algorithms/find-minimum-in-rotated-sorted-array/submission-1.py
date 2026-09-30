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
            #stop when two pointer cross 
            if nums[left]< nums[right]:
                # if the number on the left is less than number on the right , then store the left(aka min of that range) as a min 

                res = min(res,nums[left])

                break 
            mid = (right+left)//2
            res = min(res,nums[mid])
            # see if mid is the min value too 
            # the rotated portion takes the highest values and moves it to the front so 
            # the lowest values are in the right hand side 
            # if we see the mid is less than the left value, then were in the left half and need to move left pointer all the way to mid to be in the right side
            # if we see the mid is greater than the left value( normal binary search behavior)
            # then we move the right pointer to mid and search the left half
        
            if nums[mid] >= nums[left]:
                left = mid +1
            else:
                right= mid-1 

        return res

        