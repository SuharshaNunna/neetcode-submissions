class Solution:
    def countBits(self, n: int) -> List[int]:
        # can do bin conversion and then load into array or divide by two at eahch step ... brute force 
        '''
        ans= [0]*(n+1)
        for j in range(n+1):
            i=j 
            while i:
                ans[j] += i % 2
                i = i//2
        return ans
        '''
    #dp implimentation,
        dp= [0] *(n+1)
        offset = 1
        for i in range( 1, n+1):
            if offset *2 == i :
                offset =i
            dp[i]= 1+ dp[i-offset]
        return dp

