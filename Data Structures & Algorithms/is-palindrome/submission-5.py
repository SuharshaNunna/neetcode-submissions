class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        input: s = string 
        return bool

        A palindrome is a string that reads the same forward and backward
        - order does matter 

        case-insensitive 
        ignores all non-alphanumeric characters
        - ignores spaces, punctuation, symbols 

        summary: return if the char in a string are the same order read front and back 
        - can reverse the string, then compare reversed version to original version
            - need to iteratr through, load into another space( array) then make back to string then compare 
        - can start at mid point and compare left and right char until going through the whole strign 
            - need to go through string at least once to find midpoint ( also probaly needd to load into array )
        - can start at each end, compare first and last and iteraate though until first == last 
            - 1 <= s.length <= 1000 O(n) time complexity 
            - end of funct :
                - first == last  return true 
                - last< first return false -- went to far 
                * last and first are pointers 
                - would need to make 
        '''
        
        slist = [char.lower() for char in s if char.isalnum()]
        first, last = 0, (len(slist)-1)
        #return slist == slist[::-1]
        print(slist,first,last)
        while last >= first:
            if slist[first] == slist[last]:
                first +=1 
                last -=1 
            else:
                return False
        return True 

    



