class Solution:
    def findDiagonalOrder(self, matrix: 'List[List[int]]') -> 'List[int]'':
        m, n = len(matrix), len(matrix[0]) if matrix else 0
        ans = []
        for s in range(m+n-1):
            if s % 2 == 1:
                for t in range(max(s-n, 0), min(s+1, m)):
                    ans.append(matrix[t][s-t])
            else:
                for t in range(max(s-m, 0), min(s+1, n)):
                    ans.append(matrix[s-t][t])
        return ans
            
matrix = [[1,2,3],[4,5,6],[7,8,9]]
s = Solution()
ans = s.findDiagonalOrder(matrix)
print(ans)