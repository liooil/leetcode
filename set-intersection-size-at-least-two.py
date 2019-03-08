class Solution:
    def intersectionSizeTwo(self, intervals: 'List[List[int]]') -> int:
        ans = [1e8, 1e8]
        cnt = 0
        for s, e in sorted(intervals, key=lambda intv: ~intv[0]):
            if e < ans[1]:
                ans = [s, ans[0]]
                cnt += 1
                if e < ans[1]:
                    ans[1] = s+1
                    cnt += 1
        return cnt

intervals = [[1,2],[2,3],[2,4],[4,5]]

s = Solution()
ans = s.intersectionSizeTwo(intervals)
print(ans)