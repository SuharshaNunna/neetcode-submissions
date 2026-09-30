class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
#brute: combine digits array for one number and add 1 and then split it back into an array

# only add one to the last element and if that element turns into to 10 incriment the next value by one as well ( keep going until reaching end)
# we should be able to append the list if it exceeds the og size

        for i in reversed(range ( len(digits))):
            digits[i] += 1
            if digits[i] >= 10:
                digits[i]= 0
                if i == 0:
                    digits.insert(0,1)
                   
                    return digits
                
            else:
    
                return digits
        