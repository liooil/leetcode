import itertools
class Solution:
    def numSimilarGroups(self, A: 'List[str]') -> int:
        Parent = {a: a for a in A}
        def find(i):
            if Parent[i] == i:
                return i
            Parent[i] = find(Parent[i])
            return Parent[i]
        def isSimiliar(a, b):
            cnt = 0
            for ca, cb in zip(a, b):
                if ca != cb:
                    if cnt == 2:
                        return False
                    cnt += 1
            return cnt == 2
        N, W = len(A), len(A[0]) if A else 0
        if N < W:
            for a, b in itertools.combinations(Parent.keys(), 2):
                a0, b0 = find(a), find(b)
                if a0 != b0 and isSimiliar(a, b):
                    Parent[b0] = a0
        else:
            for a in Parent.keys():
                for i, j in itertools.combinations(range(W), 2):
                    b = a[:i] + a[j] + a[i+1:j] + a[i] + a[j+1:]
                    if b in Parent:
                        a0, b0 = find(a), find(b)
                        if a0 != b0 and isSimiliar(a, b):
                            Parent[b0] = a0
        return sum(a == a0 for (a, a0) in Parent.items())

A = ["tars","rats","arts","star"]
s = Solution()
ans = s.numSimilarGroups(A)
print(ans)