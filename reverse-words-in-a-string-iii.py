class Solution:
    def reverseWords(self, s: str) -> str:
        stack = []
        ans = []
        for c in s:
            if c == ' ':
                a = ''
                while stack:
                    a += stack.pop()
                ans.append(a)
                stack = []
            else:
                stack.append(c)
        a = ''
        while stack:
            a += stack.pop()
        ans.append(a)
        stack = []
        return ' '.join(ans)