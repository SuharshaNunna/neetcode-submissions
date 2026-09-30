class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
      #given 2d grid , any group of ones represents a island ( horizonticaly and vertically) 
      # zeropadded all around 
      # once an island is reached explore all the connectings pathways and change the visted to 0 

      # to explore the pathways, once we reach an 1 in the matrix explore vertical and horizontal pathways 

        islands = 0
        if not grid:
            return islands 
            #check if the grid is even valid
        
#dfs should come before rest of the functions because it needs to reference it 
        def dfs(r,c): # r and c are passed as sep elements so () : used for function calls, tuples and operations
            if (r<0 or c< 0  or r>=rows or c>= cols or grid[r][c]=="0" ): # checks if elements in range first then if its valid  
                return 
            grid[r][c]= "0"
            # need to use [][] when indexing/creating lists or dicts 
        #marked as visited 
        #technially do not need to make it set if just update to 0 
            for dr , dc in directions:
                dfs(r+dr,c+dc) # explore all posible directions though recursion 

        rows, cols= len(grid), len(grid[0])
        #rows are the lengthj of gride while colums are the length of the first element of grid
        directions= [[1,0], [-1,0],[0,1],[0,-1]]
        #possible directiosn it can move

        #to go through each elemetn need to go through all the rows and all the collums possiblilies 
        for r in range(rows):
            for c in range(cols):
                #[] for indexing 
                if grid[r][c] == "1":
                    dfs(r,c)
                    #() for function calls 
                    islands+=1
        return islands

        


