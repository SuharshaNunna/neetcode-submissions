class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # identify the anagrams and return anagrams together 
        # anagrams: have the same number of occurances for each letter
        # make an array with the occurances of each letter, make that the key for the hash map, the strings that match the key are thn added as values 
        chartostring= defaultdict(list)

        for s in strs:
            countarray= [0]*26
            for character in s:
                countarray[ord(character)- ord("a")] += 1

            chartostring[tuple(countarray)].append(s)

        return chartostring.values()

