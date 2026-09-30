class Solution:
    def climbStairs(self, n: int) -> int:

    #given end sum, need to find as many ways as we can to get there using only 2 and 1, 
    #returning an int which is count of ways to get to sum
    #Brute : use recursion to go though each pathway of the tree and return the pathways that get to n 
    #DP problem: fibonacci sequence 
    #top down : set an list to hold cache (size n) all -1 
    #when calculating the how many results the starting point will give, store that in the index of 
    #the cache, if you ever come across the same number again then just return that caches result stored in the array 

#    bottom up : if n is 2 or less just return n 
 #   initialize and array to be 0 and size n+1
  #  set index 1 and index 2 = 1 and 2 
   # go through a loop from 3 to the n+1 end of the array 
#    calcaulte the correct index's value using recursion of adding two elements before it together to get the 
 #   correct number for that index ( aka fibbonaci ) 

#    space optimized : one and two are 1 since it takes 1 move to get to the next to its number
 #   go though the n -1 since last two elements already filled out 
  #  set two to one and add one to two (prev), returning one will give you summation of all posible ways 


        one, two= 1,1
        for i in range(n-1):
            temp=one
            one=one+two
            two=temp

        return one