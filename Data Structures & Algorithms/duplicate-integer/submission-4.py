class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #add to a set and if its in the set already then return false 
        numset= []
        for n in nums: 
            if n in numset:
                return True
            else:
                numset.append(n)
            
        return False 
        