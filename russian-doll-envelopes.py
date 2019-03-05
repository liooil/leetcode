import bisect

class Solution:
    def maxEnvelopes(self, envelopes: 'List[List[int]]') -> int:
        envelopes.sort(key=lambda env: (env[0], ~env[1]))
        DP = []
        for _, n in envelopes:
            idx = bisect.bisect_left(DP, n)
            if idx == len(DP):
                DP.append(n)
            else:
                DP[idx] = n
        return len(DP)

envelopes = [[1, 1], [1, 2], [1, 3]]
s = Solution()
ans = s.maxEnvelopes(envelopes)
print(ans)