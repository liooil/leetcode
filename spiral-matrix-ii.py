class Solution:
    def generateMatrix(self, n: int) -> 'List[List[int]]':
        ans = [[None for j in range(n)] for i in range(n)]
        i, j = 0, 0
        i_lo, i_hi, j_lo, j_hi = 0, n-1, 0, n-1
        x = 1
        while x <= n*n:
            for j in range(j_lo, j_hi+1):
                ans[i_lo][j] = x
                x += 1
            i_lo += 1
            for i in range(i_lo, i_hi+1):
                ans[i][j_hi] = x
                x += 1
            j_hi -= 1
            for j in reversed(range(j_lo, j_hi+1)):
                ans[i_hi][j] = x
                x += 1
            i_hi -= 1
            for i in reversed(range(i_lo, i_hi+1)):
                ans[i][j_lo] = x
                x += 1
            j_lo += 1
        return ans

s = Solution()
ans = s.generateMatrix(4)
print(ans)