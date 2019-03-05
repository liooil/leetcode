class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        dA = [A[i+1] - A[i] for i in range(len(A)-1)]
        ddA = [dA[i+1] - dA[i] for i in range(len(dA)-1)]
        ans = cnt = 0
        for dd in ddA:
            if dd == 0:
                cnt += 1
                ans += cnt
            else:
                cnt = 0
        return ans