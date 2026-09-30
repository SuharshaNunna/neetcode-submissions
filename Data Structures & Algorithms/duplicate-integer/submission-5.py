class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #set manipulation 
        return(len(set(nums)) != len(nums))
        