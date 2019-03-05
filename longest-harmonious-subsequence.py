class Solution:
    def findLHS(self, nums: List[int]) -> int:
        D = {}
        for n in nums:
            D[n] = D.get(n, 0) + 1
        return max(
            (D[n]+D[n+1] for n in D if n+1 in D),
            default=0
        )