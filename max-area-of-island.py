class Solution:
    def maxAreaOfIsland(self, grid: 'List[List[int]]') -> 'int':
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    stack = [(i, j)]
                    grid[i][j] = 0
                    cnt = 1
                    while stack:
                        ii, jj = stack.pop()
                        for iii, jjj in (ii-1,jj), (ii+1,jj), (ii,jj-1), (ii,jj+1):
                            if 0 <= iii < m and 0 <= jjj < n:
                                if grid[iii][jjj] == 1:
                                    stack.append((iii,jjj))
                                    grid[iii][jjj] = 0
                                    cnt += 1
                    ans = max(ans, cnt)
        return ans
                                
if __name__ == "__main__":
    s = Solution()
    ans = s.maxAreaOfIsland([[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]])
    print(ans)