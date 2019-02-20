class Solution:
    def reverseVowels(self, s: 'str') -> 'str':
        VOWELS = "aeiouAEIOU"
        def getPos(s):
            for i in range(len(s)):
                if s[i] in VOWELS:
                    yield i
        def getChr(s):
            for a in reversed(s):
                if a in VOWELS:
                    yield a
        L = list(s)
        for i, a in zip(getPos(s), getChr(s)):
            L[i] = a
        return ''.join(L)