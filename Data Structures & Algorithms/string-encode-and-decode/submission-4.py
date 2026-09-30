class Solution:
#naive solution:  just combine string with delimiter ',' and then identify the delimiter
# naive solution is hard since neet to picka spesficic delimiter ...
    def encode1(self, strs: List[str]) -> str:
        total = '#'
        for s in strs:
            total+= s +'#'
        return total 
    def decode1(self, s: str) -> List[str]:
        list= []
        word= ''
        for ch in s: 
            if ch !="#":
                word += ch 
            else:
                list.append(word)
                word =''
        list.append(word)
        return list[1:-1]
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
        return res
