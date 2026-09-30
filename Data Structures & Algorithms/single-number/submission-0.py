class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # identify integer that only appears once 
        # all others appear twice

        #HASHSET EXAMPLE
#       hashset= set()
 #         if n in hashset:
   #             hashset.remove(n)
  #          else:
   #             hashset.add(n)
    #    
     #   return list(hashset)[0]

        res= 0 
        for n in nums: 
            res=n ^ res
        return res







