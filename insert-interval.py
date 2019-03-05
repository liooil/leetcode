# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # return index of first interval before v (0 if nothing before)
    # return if it is inside that interval
    def locateInIntv(self, intervals: 'List[Interval]', v: int) -> 'int, bool':
        L, H = 0, len(intervals)
        while L < H:
            M = (L+H)//2
            if v < intervals[M].start:
                H = M
            else:
                L = M+1
        return L, L and v <= intervals[L-1].end
            
    def insert(self, intervals: 'List[Interval]', newInterval: Interval) -> 'List[Interval]':
        k_s, r_s = self.locateInIntv(intervals, newInterval.start)
        k_e, r_e = self.locateInIntv(intervals, newInterval.end)
        if r_s:
            newInterval.start = intervals[k_s-1].start
            k_s -= 1
        if r_e:
            newInterval.end   = intervals[k_e-1].end
        return intervals[:k_s] + [newInterval] + intervals[k_e:]