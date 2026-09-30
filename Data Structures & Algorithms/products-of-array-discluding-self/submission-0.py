class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 48 : nums[0]= 1 output[0]= 48/1; nums[1]=2 output[2]= 48/2
        # O(n) O(1) suf      pre*suf    pre
        # transform the problem into a onlt two multiplicand
        res= [1] * len(nums)
        prefix =1 
        for i in range (len(nums)):
            #place prefix in result array then muliple my by neew numebr added 
            res [i] = prefix
            prefix *= nums[i]
        post=1 
        for i in range (len(nums) -1, -1,-1):   #statrt at end and go uptill the begiing 
            res[i]*= post
            post *= nums[i]
        return res

        

        