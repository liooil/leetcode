import bisect

class Solution:
    def lengthOfLIS(self, nums: 'List[int]') -> int:
        DP = []
        for n in nums:
            idx = bisect.bisect_left(DP, n)
            if idx == len(DP):
                DP.append(n)
            else:
                DP[idx] = n
        return len(DP)

nums = [-2, -1]
s = Solution()
ans = s.lengthOfLIS(nums)
print(ans)