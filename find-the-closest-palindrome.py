class Solution:
    def nearestPalindromic(self, n: str) -> str:
        N, r = divmod(len(n), 2)
        def str_sum(a: str, b: int) -> str:
            return str(int(a) + b)
        def getCands(n):
            
        if not N:
            return str_sum(n, -1)
        if n[0] == '1' and all(i == '0' for i in n[1:-1]) and n[-1] in "01":
            return '9' * (len(n)-1)
        if all(i == '9' for i in n):
            return str_sum(n, 2)
        if r == 0:
            ans0 = n[:N] + n[:N][::-1]
            if ans0 == n:
                ans0 = '0'
            ans1 = str_sum(n[:N], -1) + str_sum(n[:N], -1)[::-1]
            ans2 = str_sum(n[:N], 1) + str_sum(n[:N], 1)[::-1]
        else:
            ans0 = n[:N] + n[N] + n[:N][::-1]
            if ans0 == n:
                ans0 = '0'
            ans1 = '0' if n[N] == '0' else n[:N] +  str_sum(n[N], -1) + n[:N][::-1]
            ans2 = '0' if n[N] == '9' else n[:N] +  str_sum(n[N], 1) + n[:N][::-1]
        return str(min(
            (ans1, ans0, ans2),
            key=lambda ans: abs(int(ans) - int(n))
        ))

s = Solution()
ans = s.nearestPalindromic("1837722381")
print(ans)