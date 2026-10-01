class Solution:
    def countBits(self, n: int) -> List[int]:
    # can do bin conversion and then load into array or divide by two at eahch step 
        ans= [0]*(n+1)
        for j in range(n+1):
            i=j 
            while i:
                ans[j] += i % 2
                i = i//2
        return ans