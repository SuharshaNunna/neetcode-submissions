class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # board at max is 5,5 ; word at max is 10 ; all lowercase or uppercase letters
        #brute force: scan from first colum to last, first row to last looking for first letter 
        # of word, once letter matches, scan left right up and down for next leter, and so on until, word runs out of characters or next character cannot be found
        
        #finding the first letter
        # can generazise the scan method (dfs)  also need to keep track of current path 
        #getting dimentions 
        rows,cols= len(board), len(board[0])
        #keeping track of positions 
        path = set()

        #backtracking algo
        #1. nested dfs 
        def dfs(r,c,i):
            if i == len(word):
                return True 
            if (r<0 or c<0 or r>=rows or c>=cols or word[i] != board[r][c] or (r,c) in path):
                return False
            path.add((r,c))
            res=(dfs(r+1,c,i+1) or dfs(r-1,c,i+1) or dfs(r,c+1,i+1) or dfs(r,c-1,i+1))
            path.remove((r,c))
            return res

            #2. go though the positons and run dfs on it
        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0):
                    return True 

        return False

            

