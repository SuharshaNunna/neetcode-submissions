class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Brute
        #compare the first element with every other element to see if it 
        # sums to target, if not moving on to the next and such 

    # nums[i]+nums[j]= target ... target-nums[i]=nums[j]

    # create a hashmap of target- nums[i], and as we create then check in nums[j] is in the difference 

        elements = {}

        for i, number in enumerate(nums):
            diff=target-number
            if diff in elements:
                return [elements[diff], i]
            elements[number]=i
            # key is number and iterations is value 
