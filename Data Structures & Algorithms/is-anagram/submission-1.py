class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # letter: freq of letter
        dicts, dictt= {}, {} 
        for w in s:
            if w not in dicts:
                dicts.update({w:1})
            else:
                dicts[w]+=1
        for d in t:
            if d not in dictt:
                dictt.update({d:1})
            else:
                dictt[d]+=1
        return(dicts==dictt)

