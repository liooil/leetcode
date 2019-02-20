import heapq
class Solution:
    def maxWidthRamp(self, A: 'List[int]') -> 'int':
        As = [(a, i) for i, a in enumerate(A)]
        As.sort()
        idxMin = As[0][1]
        ans = 0
        for _, idx in As:
            if idx > idxMin:
                ans = max(ans, idx-idxMin)
            else:
                idxMin = idx
        return ans
A = [9,8,1,0,1,9,4,0,4,1]
s = Solution()
ans = s.maxWidthRamp(A)
print(ans)