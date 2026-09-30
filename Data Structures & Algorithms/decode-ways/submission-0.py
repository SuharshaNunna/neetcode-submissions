class Solution:
    def numDecodings(self, s: str) -> int:
# only need to return the count of ways( dont need to store values themself)
# base : each digit (except 0) byitself decoded into  letter 
# various ways to group
# restrictions: leading 0 disqualify, only two digits together, values 1-26 

# go through the string with base, counted as one,,,0 disqualifies this from adding to count 
# next add grouping on either side
# only have two branches if the first digit is a 1 or 2 , if 2 second digit needs to be between 0-6
        dp = { len(s):1}

        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i]== "0":
                return 0 
            res= dfs(i+1)
            if (i+1<len(s)and ((s[i]=="1") or s[i]=="2" and s[i+1] in "012356")):
                res += dfs(i+2)
            dp[i]=res
            return res
        return dfs(0)

 
            
        