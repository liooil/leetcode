class Solution:
    def findLength(self, A: 'List[int]', B: 'List[int]') -> int:
        ans = 0
        for i in range(len(A)):
            for j in range(len(B)):
                cnt = 0
                while i+cnt<len(A) and j+cnt<len(B) and A[i+cnt] == B[j+cnt]:
                    cnt += 1
                ans = max(ans, cnt)
        return ans

s = Solution()
ans = s.findLength([4,1,2,3], [1,2,3])
print(ans)