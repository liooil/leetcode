import bisect
class Solution:
    def findMinDifference(self, timePoints: 'List[str]') -> 'int':
        Times = []
        MAX_DIFF = 24*60
        ans = MAX_DIFF
        for timeStr in timePoints:
            time = 60*int(timeStr[:2]) + int(timeStr[-2:])
            if not Times:
                Times = [time]
                continue
            idx = bisect.bisect(Times, time)
            if idx and Times[idx-1] == time:
                return 0
            for diff in (time - Times[idx-1], Times[idx-len(Times)] - time):
                ans = min(ans, diff % MAX_DIFF)
            Times.insert(idx, time)
        return ans