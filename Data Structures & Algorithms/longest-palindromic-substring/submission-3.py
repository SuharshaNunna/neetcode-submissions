'''
given s(string)
- s contains only digits and English letters.
return a string ( the longest  palindrome substring)
goal
- return a palidrome 
- return longest palidrome 
    - best case: the whole sgtring is a palidrome 

palindrome
reads same forward and backwards 
- first letter = last letter ... second to first letter and second to last letter same ...
- sliced in half each half equals eachother revered 
- order matter 

cases:
    multiple palidromes same lenght- return any 
    empty string =? 
    - return empty 
    is palindrome gaurenteed?
        - no garuentrred 
            - no palidrome -> returning emptry string 

s = "ababd"
check each char as a middle 
palidrosm there even adn odd 
even middle 
center = i, i+1
odd middles
 center =i
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res =''
        reslen= 0
        for i in range ( len(s)):
            l,r= i,i
            while l>=0 and r< len(s) and s[l]==s[r]:
                if (r-l+1)> reslen:
                    reslen= r-l+1
                    res=s[l:r+1]
                l-=1
                r+=1
            l,r= i,i+1
            while l>=0 and r< len(s) and s[l]==s[r]:
                if (r-l+1)> reslen:
                    reslen= r-l+1
                    res=s[l:r+1]
                l-=1
                r+=1
        return res


            
            



        