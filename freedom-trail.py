class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        D = {}
        for i, c in enumerate(ring):
            if c not in D:
                D[c] = []
            D[c].append(i)
        
        def dist(s: int, t: int):
            d = abs(t-s)
            return min(d, len(ring)-d) + 1

        curr = {0: 0}
        for c in key:
            curr = {
                currPosN: min(
                    currSteps + dist(currPos, currPosN) for (currPos, currSteps) in curr.items()
                ) for currPosN in D[c]
            }
        return min(curr.values())