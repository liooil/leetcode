class Solution:
    def isRectangleOverlap(self, rec1: 'List[int]', rec2: 'List[int]') -> 'bool':
        xs1, ys1, xt1, yt1 = rec1
        xs2, ys2, xt2, yt2 = rec2
        return xt1 > xs2 and xt2 > xs1 and yt1 > ys2 and yt2 > ys1