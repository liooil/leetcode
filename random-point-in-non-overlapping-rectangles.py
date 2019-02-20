import random, bisect
class Solution:

    def __init__(self, rects: 'List[List[int]]'):
        self.rects = rects
        points = [0]
        for xs, ys, xt, yt in rects:
            points.append((xt-xs+1)*(yt-ys+1) + points[-1])
        self.areas = points

    def pick(self) -> 'List[int]':
        d = random.randint(0, self.areas[-1]-1)
        rec_idx = bisect.bisect(self.areas, d)-1
        xs, ys, xt, yt = self.rects[rec_idx-1]
        r = d - self.areas[rec_idx]
        xr, yr = divmod(r, xt-xs+1)
        return [xs+xr, ys+yr]

# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()