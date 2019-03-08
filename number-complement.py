class Solution:
    def findComplement(self, num: int) -> int:
        for i in range(32):
            if num >= 1<<i:
                num ^= 1<<i
            else:
                break
        return num