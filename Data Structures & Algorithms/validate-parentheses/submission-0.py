class Solution:
    def isValid(self, s: str) -> bool:
        # add each element to the stack
        # until the next elements pair is already in the stack (open in stack with close about to be added)
        #^ if that is identified pop the previous element
        # if the string runs out eith nothing in the stack then it is true, if therese element left in the stack then it is false 

        stack= []
        #create a dictornary of close to open characters

        closetoopen={")":"(","]":"[","}":"{"}
      #close is ket and open is value
        for bracket in s:
            if bracket in closetoopen:
                if stack and stack[-1]== closetoopen[bracket]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)
        return True if not stack else False
 
        