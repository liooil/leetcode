class Solution:
    def originalDigits(self, s: str) -> str:
        ans = [0 for i in range(10)] # zero one two three four five six seven eight nine
        for c in s:
            if c == 'z': # zero
                ans[0] += 1
                ans[1] -= 1
            elif c == 'w': # two
                ans[2] += 1
                ans[1] -= 1
            elif c == 'u': # four
                ans[4] += 1
                ans[1] -= 1
                ans[5] -= 1
                ans[9] += 1
            elif c == 'x': # six
                ans[6] += 1
                ans[7] -= 1
                ans[9] -= 1
            elif c == 'g': # eight
                ans[8] += 1
                ans[3] -= 1
                ans[9] -= 1
            elif c == 'o': # one
                ans[1] += 1
            elif c == 'h': # three
                ans[3] += 1
            elif c == 'f': # five
                ans[5] += 1
                ans[9] -= 1
            elif c == 's': # seven
                ans[7] += 1
            elif c == 'i': # nine
                ans[9] += 1
        return ''.join(n*"0123456789"[i] for i, n in enumerate(ans))


s = Solution()
ans = s.originalDigits("one")