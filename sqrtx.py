class Solution:
    def mySqrt(self, x: int) -> int:
        r = x
        while r ** 2 > x:
            r = (r + x//r) // 2
        return r
        
s = Solution()
ans = s.mySqrt(6)
print(ans)