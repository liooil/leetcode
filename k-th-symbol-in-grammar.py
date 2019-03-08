class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        k = K-1
        ans = 0
        while k:
            if k & 1:
                ans ^= 1
            k >>= 1
        return ans