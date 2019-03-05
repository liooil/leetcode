class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        N = len(nums)
        S = set(range(1, N+1))
        Ans = [0, 0]
        for n in nums:
            if n in S:
                S.remove(n)
            else:
                Ans[0] = n
        Ans[1] = S.pop()
        return Ans