class Solution:
    def uniquePathsIII(self, grid: 'List[List[int]]') -> 'int':
        m, n = len(grid), len(grid[0]) if grid else 0
        X = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    i0, j0 = i, j
                elif grid[i][j] == 0:
                    X += 1
        def DFS(X: 'int', x, y: 'tuple(int, int)'):
            ans = 0
            grid[x][y] = -2
            for xx, yy in (x-1, y), (x+1, y), (x, y+1), (x, y-1):
                if 0 <= xx < m and 0 <= yy < n:
                    if grid[xx][yy] == 2:
                        if X == 0:
                            ans += 1
                    elif grid[xx][yy] == 0:
                        ans += DFS(X-1, xx, yy)
            grid[x][y] = 0
            return ans
        return DFS(X, i0, j0)

s = Solution()
ans = s.uniquePathsIII(
    
)