class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #same amount of letters
        #both words need the exact same amount of each letter 
        #Order doesnt matter -> set and dict, need to keep track of amount of each letter so dict
        sdict={}
        tdict={}
        for l in s:
            if l in sdict:
                sdict[l] +=1
            else:
                sdict[l]=1
        for l in t:
            if l in tdict:
                tdict[l] +=1 
            else:
                tdict[l]=1
        return (sdict==tdict)

        