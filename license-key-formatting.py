class Solution:
    def licenseKeyFormatting(self, S: 'str', K: 'int') -> 'str':
        stack = []
        for s in reversed(S):
            if s != '-':
                s = s.upper()
                if not stack or len(stack[-1]) == K:
                    stack.append(s)
                else:
                    stack[-1] = s + stack[-1]
        stack.reverse()
        return '-'.join(stack)