class Solution:
    def pacificAtlantic(self, matrix: 'List[List[int]]') -> 'List[List[int]]':
        m, n = len(matrix), len(matrix[0]) if matrix else 0
        def getAdjs(i, j):
            return [
                (ii, jj) for ii, jj in (
                    (i-1,j), (i+1,j), (i,j-1), (i,j+1)
                ) if 0<=ii<m and 0<=jj<n and matrix[i][j] <= matrix[ii][jj]
            ]

        Pac = {(i, j) for i in range(m) for j in range(n) if i==0 or j==0}
        pacs = [(i, j) for i in range(m) for j in range(n) if i==0 or j==0]
        while pacs:
            i, j = pacs.pop()
            for ii, jj in getAdjs(i, j):
                if (ii, jj) not in Pac:
                    Pac.add((ii, jj))
                    pacs.append((ii, jj))
        Alt = {(i, j) for i in range(m) for j in range(n) if i==m-1 or j==n-1}
        alts = [(i, j) for i in range(m) for j in range(n) if i==m-1 or j==n-1]
        while alts:
            i, j = alts.pop()
            for ii, jj in getAdjs(i, j):
                if (ii, jj) not in Alt:
                    Alt.add((ii, jj))
                    alts.append((ii, jj))
        return list(Pac & Alt)