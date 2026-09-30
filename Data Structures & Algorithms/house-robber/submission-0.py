class Solution:
    def rob(self, nums: List[int]) -> int:
        # goal to get the most money without alerating 
        # if we go for the highest then 3,4,3 would fail as 3 and 3 would be better
        rob1, rob2 = 0,0 
        # rob1, rob2, n, n+1,...
        for n in nums:
            temp= max(n+rob1,rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
    

        