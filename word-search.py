import collections
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0]) if board else 0
        
        def DFS(path):
            if len(path) == len(word):
                return True
            i, j = path[-1]
            for ii, jj in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
                if 0 <= ii < m and 0 <= jj < n and board[ii][jj] == word[len(path)]:
                    if (ii, jj) in path:
                        continue
                    if DFS(path + [(ii, jj)]):
                        return True
            return False        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if DFS([(i, j)]):
                        return True
        return False