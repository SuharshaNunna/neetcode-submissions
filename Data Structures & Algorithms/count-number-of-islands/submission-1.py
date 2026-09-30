class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
      #given 2d grid , any group of ones represents a island ( horizonticaly and vertically) 
      # zeropadded all around 
      # once an island is reached explore all the connectings pathways and change the visted to 0 

      # to explore the pathways, once we reach an 1 in the matrix explore vertical and horizontal pathways 

        islands = 0
        #if not grid:
            #return islands 
            #check if the grid is even valid
        def dfs(r,c):
            if (r<0 or c< 0  or r>=rows or c>= cols or grid[r][c]=="0" ):
                return 
            grid[r][c]= "0"
        #marked as visited 
        #techniall do not need to make it set if just update to 0 
            for dr , dc in directions:
                dfs(r+dr,c+dc)


        rows, cols= len(grid), len(grid[0])
        directions= [[1,0], [-1,0],[0,1],[0,-1]]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(r,c)
                    islands+=1
        return islands

        


