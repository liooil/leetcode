class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        it = reversed(s)
        ans = 0
        try:
            while next(it) == ' ':
                pass
            ans = 1
            while next(it) != ' ':
                ans += 1
        except StopIteration:
            pass
        return ans