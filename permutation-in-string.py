class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        D = {}
        for c in s1:
            if c not in D:
                D[c] = 0
            D[c] -= 1
        for c in s2[:len(s1)]:
            if c not in D:
                D[c] = 0
            D[c] += 1
            if D[c] == 0:
                del D[c]
        if not D:
            return True
        for c0, c in zip(s2, s2[len(s1):]):
            if c == c0:
                continue
            if c not in D:
                D[c] = 0
            D[c] += 1
            if c0 not in D:
                D[c0] = 0
            D[c0] -= 1
            if D[c] == 0:
                del D[c]
            if D[c0] == 0:
                del D[c0]
            if not D:
                return True
        return False