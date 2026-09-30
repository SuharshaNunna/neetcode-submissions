class Solution:
    def longestPalindrome(self, s: str) -> str:
# only need to store the biggest palindrome 
#requirement: first letter = last letter  ( i= -i, i+1 , = -i-1) no beacuse it could be off centerd 
# center check each letter to be the center and keep track ofbiggets in varbible 

        resIdx = 0
        resLen=0
        size = len(s)
        for i in range( size):
            l,r=i,i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resIdx = l
                    resLen = r - l + 1
                l -= 1
                r += 1
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resIdx = l
                    resLen = r - l + 1
                l -= 1
                r += 1

        return s[resIdx : resIdx + resLen]




        