'''
return the minimum element of this array in O(log n) time
 given nums array - was once sorted now has been rotated 1 to n times 

 rotated  - each rotation takes last element and moves it to the front 
the minimum is at the intersection of rotated and unrotated part 
how to identify which is rotated and unrotated 
[3,4,5,6,1,2]
logn-> binary search 
left 3 right 2  mid 5 
if left >mid -> rotated   no 
if right< mid -> rotated  yes 
we want rotated secotion  
move left 5 right 2  mid 6
if left >mid -> rotated   no 
if right< mid -> rotated  yes 
left 6 right 2 mid 1 
if left >mid -> rotated   yes 
if right< mid -> rotated  no 
right 1 left 6 mid 1 
if left >mid -> rotated   yes 
if right< mid -> rotated  no
left 6  return mid  
identify which half is rotated 
reverse logic on that half
'''
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r= 0, (len(nums)-1)
        while l<r:
            m= l + (r - l) // 2
            if nums[r] <nums[m]:
                l=m+1
            else:
                r=m
        return nums[r]



        