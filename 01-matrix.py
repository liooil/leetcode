class Solution:
    def updateMatrix(self, matrix: 'List[List[int]]') -> 'List[List[int]]':
        m, n = len(matrix), len(matrix[0])
        ans = [[None if c else 0 for c in line] for line in matrix]
        queue = [(i,j) for i in range(m) for j in range(n) if matrix[i][j]==0]
        for d in range(1, m+n):
            queueN = []
            for i, j in queue:
                for ii, jj in (i-1,j), (i+1,j), (i,j-1), (i,j+1):
                    if 0<=ii<m and 0<=jj<n and ans[ii][jj] == None:
                        ans[ii][jj] = d
                        queueN.append((ii, jj))
            queue = queueN
            if not queue:
                break
        return ans