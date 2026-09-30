class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # stones : list, output is last stone value 
        # order does not matter
        # Brute: identify the two largest stones, then do comparaisons and functions to return the result -> keep going until one element in the lis t

        # max heap: 
        # take the two largets in the function then pop both of them, push= the result of the operatation 
        # if == u dont push anything
        # if != then take differnece -> push that difference on to the max heap 
        # keep doing push and poping untill there is only one elemetn in the heap( length of 1 )
        
     
        stones =[s*-1 for s in stones]
        heapq.heapify(stones)
        # 0 index would be the max
        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            if not x==y:
                x = abs(y-x)
                heapq.heappush(stones,x*-1)
            else:
                heapq.heappush(stones,0)
            print(stones)

        if stones[0]< 0:
            stones[0]=stones[0] * -1
        return (stones[0])



        