class Solution:
    def strWithout3a3b(self, A: int, B: int) -> str:
        ans = ""
        if A >= B:
            while A > B and A > 2:
                ans += 'aab'
                A -= 2
                B -= 1
        else:
            while B > A and B > 2:
                ans += 'bba'
                B -= 2
                A -= 1
        while A and B:
            ans += 'ab'
            B -= 1
            A -= 1
        ans += 'b'*B + 'a'*A
        return ans