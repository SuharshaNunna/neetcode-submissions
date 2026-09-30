class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numdict={}
        for i in range(len(nums)):
            goal= target-nums[i]
            if goal in numdict:
                return [numdict[goal],i]
            else:
                numdict[nums[i]]=i
        