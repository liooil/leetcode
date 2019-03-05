class Solution:
    def shortestBridge(self, A):
        def getAdjs(i, j):
            for ii, jj in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
                if 0 <= ii < n and 0 <= jj < n:
                    yield ii, jj
        def dfs(i, j):
            A[i][j] = -1
            queue.append((i, j))
            for ii, jj in getAdjs(i, j):
                if A[ii][jj] == 1:
                    dfs(ii, jj)
        def first():
            for i in range(n):
                for j in range(n):
                    if A[i][j]:
                        return i, j
        n, step, queue = len(A), 0, []
        dfs(*first())
        while queue:
            queueN = []
            for i, j in queue:
                for ii, jj in getAdjs(i, j):
                    if A[ii][jj] == 1:
                        return step
                    elif A[ii][jj] == 0:
                        A[ii][jj] = -1
                        queueN.append((ii, jj))
            step += 1
            queue = queueN

s = Solution()
ans = s.shortestBridge(
    [[0,1],[1,0]]
)
print(ans)