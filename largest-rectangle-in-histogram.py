class Solution:
    def largestRectangleArea(self, heights: 'List[int]') -> int:
        # height, area
        heights.append(0)
        N = len(heights)
        ans = 0
        mins = []
        for j in range(N):
            i = j
            while mins and mins[-1][0] > heights[j]:
                h, i = mins.pop()
                ans = max(ans, (j-i)*h)
            mins.append((heights[j], i))
        return ans

heights = [1]
s = Solution()
ans = s.largestRectangleArea(heights)
print(ans)