class Solution:
    def isHappy(self, n: int) -> bool:
#so square each digit in the number and add up 
# keep going until you get to one or get to a number that has been already calculated 

# need a set to keep track of previous sums,
# need to figure out how to add all sep digits ( can use mod) or  string conversion 
        def getdigit(n):
            total = 0
            while n > 0:
                if n < 10:
                    total += n**2
                    break
                total += (n%10)**2
                n //=10
            return total
        seennums= set()
        while n != 1:
            n = getdigit(n)
            if n in seennums:
                return False
            seennums.add(n)
    
        return True 


        
    