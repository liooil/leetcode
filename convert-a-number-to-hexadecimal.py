class Solution:
    def toHex(self, num: 'int') -> 'str':
        ans = ""
        for _ in range(8):
            num, r = divmod(num, 16)
            ans = "0123456789abcdef"[r] + ans
            if num == 0:
                break
        return ans