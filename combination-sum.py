class Solution:
    def combinationSum(self, candidates: 'List[int]', target: int) -> 'List[List[int]]':
        candidates.sort(reverse=True)
        memo = {}
        def helper(idx: int, target: int):
            if target == 0:
                return [()]
            elif idx == len(candidates):
                return []
            if (idx, target) not in memo:
                memo[(idx, target)] = []
                for i in range(target//candidates[idx]+1):
                    for comb in helper(idx+1, target - candidates[idx]*i):
                        memo[(idx, target)].append(
                            (i,) + comb
                        )
            return memo[(idx, target)]
        
        ans = []
        for comb in helper(0, target):
            ans.append([])
            for n, c in zip(comb, candidates):
                ans[-1] += [c]*n
        return ans

candidates = [2,3,6,7]
target = 7
s = Solution()
ans = s.combinationSum(candidates, target)
print(ans)