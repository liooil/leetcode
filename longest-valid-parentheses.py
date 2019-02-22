class Solution:
    def longestValidParentheses(self, s: 'str') -> 'int':
        ans, Lefts = 0, [-1]
        for i, c in enumerate(s):
            if c == ')':
                Lefts.pop()
                if Lefts: # successfully paired
                    ans = max(ans, i - Lefts[-1])
                    continue
            Lefts.append(i)
        return ans