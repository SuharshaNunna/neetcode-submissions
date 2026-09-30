class Solution:
    def isPalindrome(self, s: str) -> bool:
        # can use two pointer one being at the left and one at the right end 
        # if both pointer are not == then return false and exit early
        s = ''.join(c.lower() for c in s if c.isalnum())
        #^ this joins the string together if they are only valid for the problem  and . lower convert upper case to lower case 
        left = 0
        right = len(s)-1
        
        while left <= right: 
            if s[left]!= s[right]:
                return False
            else:
                left += 1
                right -= 1
        return True

