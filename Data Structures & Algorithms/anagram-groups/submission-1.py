'''
given strs 
goal: group all anagrams together into sublists


An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
- order does meatter
- freq of char is = 

dict 
key sorted words 
value strings 

o(n) 
o(m)
edge 
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return ""
        ana= {} 
        for s in strs:
            sorts= str(sorted(s))
            if sorts in ana:
                ana[sorts].append(s)
            else:
                ana[sorts]=[s]
        res=[]
        for j in ana.values():
            res.append(j)
        return res
            


        