class Solution:
    def isValid(self, s: str) -> bool:
        # String -> iterable 
        # 1. check that every open has a close bracket ... vise versa
        #2. if a bracket is open, the next item should be close or another pair of partheseis 
        # ([)], {([)]} .. not valid  ([()]).. valid 
        # sorting is uncessary 
        # 
        stack = []
        op= ("[","{","(")
        if len(s)<= 1:
            return False
        for i in s:
            if i in op:
                stack.append(i)
            elif stack:
                if i == ']':
                    if stack[-1]== '[':
                        stack.pop()
                    else:
                        return False 
                elif i == ')':
                    if stack[-1]== '(':
                        stack.pop()
                    else:
                        return False
                elif i == '}':
                    if stack[-1]== '{':
                        stack.pop()
                    else:
                        return False
            else:
                return False 
        if stack:
            return False
        else:
            return True 



        