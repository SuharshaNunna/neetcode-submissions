'''
given an array of distinct integers nums and a target integer target.

 return a list of all unique combinations of nums - numbers sum to target.

 same number may be chosen from nums
 - unlimited 

 Two combinations are the same if frequency of each of the chosen numbers is the same,
 - order does not matter

  return the combinations in any order 
order of the numbers in each combination can be in any order.
nums are distinct.
1 <= nums.length <= 20
2 <= nums[i] <= 30
- no negatives 
2 <= target <= 30

given list of number and a target, return all the ways to get that target using the numbers 
- duplicates are allowed, order matters
- return empty list is a combination cannot be made 
nums = [2,5,6,9]
target = 9
starting with 2
target -i = 7
7 is not 0 or - 
new target is 7  -> save 2 to curr list 
7-2 = 5
5 is not 0 or - 
new target is 5 -> save 2 to curr list 
5-2 = 3
3 is not 0 or - 
new target is 3 -> save 2 to curr list 
3 -2 = 1
1 is not 0 or - 
1 is new target-> save 2 to curr list 
1-2= -1 
negative value detected-- backtrack we went too far -> pop 2 from list 
target is back to 3 
3-5 = -2 
negative value detected -- backtrack -> pop form list 
target is back to 5
5-5 = 0 
0 detetcted -> combination detected -> save 5 to curr list 
append ( 2,2,5)
restet curr list
'''
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        currlist=[]
        if not nums:
            return res 
        def dfs(i,currGoal):
            if currGoal == 0:            
                res.append(currlist.copy())
                return
            if currGoal <0:
                #backtrack
                return 
            for i in range(i,len(nums)):
                currlist.append(nums[i])
                dfs(i,currGoal-nums[i])
                currlist.pop()
        dfs(0,target)             

        return res
        
                
            