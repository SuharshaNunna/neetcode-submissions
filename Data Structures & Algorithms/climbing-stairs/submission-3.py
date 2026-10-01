class Solution:
    def climbStairs(self, n: int) -> int:
        #given an int, return the distinct number of ways the to get the int using only addition and 1 or 2 
        # distinct means the order does  matter... 1+2+1 != 2+1+1
        # at each step have a choice to take 1 or 2 steps , following choice have a choice to take 1 or 2 steps 
        #data structures to consider queue, array, tree, set, dict,
        # bottom up 
        # if we start at n how many ways to get to n-> 1 way 
        one, two = 1,1
        for i in range (n-1):
            temp = one
            one = one +two 
            two = temp 
        return one


        



        


        