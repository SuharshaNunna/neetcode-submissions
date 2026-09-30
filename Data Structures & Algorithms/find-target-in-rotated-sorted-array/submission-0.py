class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # rotated; last element becomes the first element, every other element moves to the right 
        # naive solution: iterate though array( o(n)) and when match is found return index
        # take advantage of rotations , some part of the array will always be in order 
        #  we can use binary search 
        #mid left and right , if left  <mid  and target in then in sorted region, can do reg 
        # if left > mid in revsered 

        size = len(nums)
        l,r = 0,(size-1) 
        
        while l<=r:
            mid = ( r+l)//2 
            if target == nums[mid]:
                return mid
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target <nums[l]:
                    l = mid+1
                else:
                    r = mid -1
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid -1
                else:
                    l=mid +1
        return -1


        