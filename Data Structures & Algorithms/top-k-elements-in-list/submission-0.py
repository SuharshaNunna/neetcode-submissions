class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Brute: can make a new array in order of most frequent to least
        # return the number of elements that k requires 
     
        # Bucket Sorting algorithm: index of array is actually count value, and component of array is a list of numbers that occur at that count 

        length= len(nums) +1 
        hashcount = {}
        # key is numbers, value is count value
        bucket = [[] for i in range (length)]
        for n in nums:
            # .get gives u the key and its defalut assignment 
            hashcount[n] = 1 + hashcount.get(n,0)

        sol = [] 
# .items is key and value 
        for num, count in hashcount.items() :
            bucket[count].append(num)
        # now the array is in order with high indexs containng the number of highest frequency
        
        for i in range(len(bucket)-1,0,-1):
            for value in bucket[i]:
                sol.append(value) 
                if len(sol) == k:
                    return sol

