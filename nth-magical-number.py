import math
class Solution:
    def nthMagicalNumber(self, N: int, A: int, B: int) -> int:
        C = A * B // math.gcd(A, B)
        def guess(s):
            return s // A + s // B - s // C
        lo, hi = 0, N*A
        while lo < hi:
            mid = (lo + hi) // 2
            if guess(mid) < N:
                lo = mid + 1
            else:
                hi = mid
        return lo % 1000000007


s = Solution()
s.nthMagicalNumber(0, 2, 3)