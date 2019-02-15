class Solution:
    def cherryPickup(self, grid: 'List[List[int]]') -> 'int':
        m, n = len(grid), len(grid[0])
        def genLayer(layer):
            s = max(0, layer-m+1)
            e = min(layer+1, n)
            for rL in range(s, e):
                for rR in range(rL, e):
                    try:
                        yield (rL, rR), sum(
                            getCherry(r, layer) for r in {rL, rR}
                        )
                    except ValueError:
                        continue
        def getCherry(r, layer):
            x, y = layer-r, r
            if grid[x][y] >= 0:
                return grid[x][y]
            raise ValueError
        def getPrev(rs, layer):
            def getHalfPrev(r):
                if r > 0:
                    yield r-1
                if r < layer:
                    yield r
            for rrL in getHalfPrev(rs[0]):
                for rrR in getHalfPrev(rs[1]):
                    if rrL < rrR:
                        yield rrL, rrR
                    else:
                        yield rrR, rrL
        DP = {}
        try:
            DP[(0,0)] = getCherry(0, 0)
        except ValueError:
            return 0
        for layer in range(1, m+n-1):
            DPN = {}
            for rs, crs in genLayer(layer):
                for rPrev in getPrev(rs, layer):
                    if rPrev not in DP:
                        continue
                    if rs not in DPN:
                        DPN[rs] = crs + DP[rPrev]
                    else:
                        DPN[rs] = max(DPN[rs], crs + DP[rPrev])
            DP = DPN
            if not DP:
                return 0
        return DP[(m-1, n-1)]

if __name__ == "__main__":
    s = Solution()
    ans = s.cherryPickup(
        [[0,1,-1],[1,0,-1],[1,1,1]]
    )
    print(ans)