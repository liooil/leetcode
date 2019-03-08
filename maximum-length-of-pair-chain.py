import bisect
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        tails = []
        for s, e in sorted(pairs):
            idx = bisect.bisect_left(tails, s)
            if idx == len(tails):
                tails.append(e)
            tails[idx] = min(tails[idx], e)
        return len(tails)