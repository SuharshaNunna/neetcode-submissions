'''
array heights
length of array = number of bars 
value of i = height of ith bar 

goal= return max amount of water between two bars
2 <= height.length <= 100,000
0 <= height[i] <= 10,000

to get max water
- need to maximize heights of both bars
- maximize disance between both bars (width)
since area = l*w 

 go through every posibility 
 every pair calc amount of water , only update if more than max 
 nested loops 
 for i in range(len(heights-1)):
    for j in heights:


order matters - sorting doenst do anything 
do we have to go through every posibility?
height = [1,7,2,5,4,7,3,6]
l 1  r 7 
min (height[l],height[r]) = height 
width =  r-l

does moving r to the right increase or = water -> yes then move 
does moving l to right increase or = water -> yes then move 

does moving r to the right increase or = water -> no, keep right  
does moving l to right increase water or =  -> no , keep left 
 consider height and width 
o(n)
edge case:
= cases covered 
no negative 
[1,9,1,1,1,1,10]
'''
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r= 0, (len(heights)-1)
        h= min(heights[l],heights[r])
        w = r-l
        sol = h*w
        while l<r:
            h= min(heights[l],heights[r])
            w = r-l
            sol = max(sol,h*w)
            if heights[l]<=heights[r]:
                l +=1
            else:
                r-=1
        return sol
            
