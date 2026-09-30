class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 1. sort each string ( so that repeats are next to eachother)
        #2. compare each index of sorted string, if there is at least one elemement not matching then exit and return false 
        # brute force 

        # maintain the frequency in hash tables , then compare the frequency 
        if len(s) != len (t): 
            return False 
        freqs, freqt = {},{} # created two hashmaps 
 
        for i in range(len(s)): #building the hashmaps
            freqs[s[i]] = 1 + freqs.get(s[i], 0)
            freqt[t[i]] = 1 + freqt.get(t[i], 0)
#now check counts 
        for j in freqs:
            if freqs[j] != freqt.get(j,0):
                return False 
        return True
        


        
        