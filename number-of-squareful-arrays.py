import itertools, collections, math
class Solution:
    def isSqrful(self, a, b):
        return a == None or b == None or math.sqrt(a+b) % 1 == 0
    def numSquarefulPerms(self, A: List[int]) -> int:
        cnt = collections.Counter(A)
        def DFS(rem, tail):
            ans = 0
            if not rem:
                return 1
            for r in rem:
                if self.isSqrful(tail, r):
                    ans += DFS(rem - collections.Counter([r]), r)
            return ans
        return DFS(cnt, None)

