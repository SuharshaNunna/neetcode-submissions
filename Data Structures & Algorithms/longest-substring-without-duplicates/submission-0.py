class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #start with window 1 length, add to length if next char is valid
        # if next char isnt valid move window to right 
        # know valid by adding char to set to check
        # return char length 
        if not s: return 0
        l, r = 0,0
        charset= set(s[0])
        maxl = 1
        while r < len(s) - 1:
            if s[r+1] not in charset:
                r += 1
                charset.add(s[r])
                maxl = max(maxl, (r-l + 1))
            else:
                charset.remove(s[l])
                l += 1
        return maxl
