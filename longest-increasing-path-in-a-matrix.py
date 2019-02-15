class Solution:
    def longestIncreasingPath(self, matrix: 'List[List[int]]') -> 'int':
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        Increases = [[[] for i in range(m)] for j in range(n)]
        starts = {(i, j) for i in range(m) for j in range(n)}
        for i in range(m):
            for j in range(n):
                adjs = []
                if i:
                    adjs.append(((i, j), (i-1, j)))
                if j:
                    adjs.append(((i, j), (i, j-1)))
                for (i, j), (ii, jj) in adjs:
                    if matrix[i][j] == matrix[ii][jj]:
                        continue
                    elif matrix[i][j] > matrix[ii][jj]:
                        i, ii = ii, i
                        j, jj = jj, j
                    Increases[i][j].append((ii, jj))
                    starts.discard((ii, jj))
        queue = list(starts)
        for length in range(m*n):
            if not queue:
                return length
            queueN = []
            for i, j in queue:
                for ii, jj in Increases[i][j]:
                    queueN.append((ii, jj))
            queue = queueN