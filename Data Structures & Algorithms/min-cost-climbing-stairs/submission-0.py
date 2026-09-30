class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #goal: smallest total possibility to pass last index ( going over the stairs)
        # can take one or two steps , have to pay the price in the index of your current step 
         # can keep track of past pathways from a certain node, stored in a cache and call that 
         # instead of going though alll the recursive calls

        cache = [-1] * len( cost)
        def dfs(i):
            if i>=len(cost):
                return 0 
            if cache[i]!= -1:
                return cache [i]
            cache[i]=cost[i] + min(dfs(i+1),dfs(i+2))
            return cache[i]

# starting should start with either position 0 or position 1
        return min (dfs(0),dfs(1))
        