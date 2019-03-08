import collections, functools

class Solution:
    def isSubsets(self, a: str, D: dict) -> bool:
        for c in a:
            if c in D:
                D[c] -= 1
                if D[c] == 0:
                    del D[c]
                    if not D:
                        return True
        return False
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        D = {}
        for b in B:
            Db = {}
            for c in b:
                if c not in Db:
                    Db[c] = 0
                Db[c] += 1
            for c in Db:
                if c not in D or D[c] < Db[c]:
                    D[c] = Db[c]
        print(D)
        ans = []
        for a in A:
            if self.isSubsets(a, D.copy()):
                ans.append(a)
        return ans