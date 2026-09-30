class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # get all the possible combinations that make sum of three numbers that = 0
        # but all have to be distinct 

        #i + j+ k = 0
        # i = -(j+k )
#Sort list 
#iterate through i, have left pointer for j and right pointer for k 
        result=[]
        nums.sort()
        for i, v in enumerate(nums): 
            if v>0:
                break
            if i > 0 and v == nums[i-1]:
                continue
            j = i+1
            k = len(nums)-1
            while j < k:
                tsum = v+nums[j]+nums[k]
                if tsum> 0:
                    k-=1
                elif tsum< 0 :
                    j+=1
                else:
                    result.append([v , nums[j],nums[k]])
                    j+=1 
                    k -=1
                    while nums[j] == nums[j-1] and j < k:
                        j +=1
                    
        return result


        