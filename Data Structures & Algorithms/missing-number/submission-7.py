'''
given array of n ints 
- no duplicates 

return single number that is missing from nums 


given a list of numbers up till n return the missing number in the ordered array 
- length of array = n
- each number goes up by one, if not it is missing 

each ith pos = value of number 

considering edge cases 
empty -> 0 missing - covered in implimentation 
last value missing 012 when n = 3 .. 3 missing 
IMPORTANT NOTE: numbers are not in order 
- to fix this sort numbers - o(n)

nums=[3,0,1]

[0,1,3]
len = 3 
i = 0 , nums[0]= 0 ok 
i = 1 , nums[1]= 1 ok 
i = 2 , nums[2]= 3 no return i 

naive :
        nums.sort()
        for i in range (len(nums)):
            if i != nums[i]:
                return i
        return len(nums)

        another
                num=set(nums)
        for i in range (len(nums)):
            if i not in num:
                return i
        return len(nums)
'''
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xorr = len(nums)
        for i in range(len(nums)):
            xorr ^= i ^ nums[i]
        return xorr
    
        