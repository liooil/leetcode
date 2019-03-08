import math
class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        ans = int(math.log2(n))+1
        for n in nums:
            if math.log2(n) % 1 == 0:
                ans -= 1
        return ans
