class Solution:
    def kSimilarity(self, A: 'str', B: 'str') -> 'int':
        Ds = {c:{} for c in "abcdef"}
        for a, b in zip(A, B):
            if a != b:
                if b not in Ds[a]:
                    Ds[a][b] = 0
                Ds[a][b] += 1
        ans = 0
        for aid in range(6):
            for bid in range(aid):
                a, b = "abcdef"[aid], "abcdef"[bid]
                if b in Ds[a] and a in Ds[b]:
                    ans += min(Ds[a][b], Ds[b][a])
                    if Ds[a][b] > Ds[b][a]:
                        Ds[a][b] -= Ds[b][a]
                        del Ds[b][a]
                    elif Ds[a][b] < Ds[b][a]:
                        Ds[b][a] -= Ds[a][b]
                        del Ds[a][b]
                    else:
                        del Ds[b][a]
                        del Ds[a][b]
        def getLoop(Ds):
            paths = [(
                (i, j), Ds[i][j]
            ) for i in Ds for j in Ds[i]]
            while paths:
                path, l = paths.pop()
                i, j = path[0], path[-1]
                if i in Ds[j]:
                    yield path, min(l, Ds[j][i])
                for k in Ds[j]:
                    if k not in path:
                        paths.append((path+(k,), min(l, Ds[j][k])))
        def findMaxLoops(Ds):
            ans = 0
            for path, l in getLoop(Ds):
                DsN = {i:{j:Ds[i][j] for j in Ds[i]} for i in Ds}
                for i, j in zip(path, path[1:]+path[:1]):
                    DsN[i][j] -= l
                    if DsN[i][j] == 0:
                        del DsN[i][j]
                        if not Ds[i]:
                            del Ds[i]
                ans = max(ans, findMaxLoops(DsN) + l)
            return 0 if ans == None else ans
        NN = sum(Ds[i][j] for i in Ds for j in Ds[i])
        return NN-findMaxLoops(Ds) + ans

A = "aabc"
B = "abca"
s = Solution()
ans = s.kSimilarity(A, B)
print(ans)