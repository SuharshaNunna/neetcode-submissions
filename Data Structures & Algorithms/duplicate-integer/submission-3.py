class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #inputs always in order, if # to the right is the same as before 
        #then make bool false, end iterations, and return ... brute force 
# hash strat: 

        block= set()
        for x in nums:
            if x in block:
                return True
            block.add(x)
        return False 
