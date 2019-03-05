class Solution:
    def maxCoins(self, nums: 'List[int]') -> int:
        N = len(nums)
        nums.append(1)
        memo = [[None for R in range(N+1)] for L in range(N+1)]
        for R in range(N+1):
            memo[R][R] = 0
            for L in reversed(range(R)):
                memo[L][R] = max(
                    memo[L][i] + memo[i+1][R] + nums[i] * nums[L-1] * nums[R] for i in range(L, R)
                )
        return memo[0][N]

nums = [3,1,5,8]
s = Solution()
ans = s.maxCoins(nums)
print(ans)