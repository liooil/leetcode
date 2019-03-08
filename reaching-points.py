class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:        
        while tx > sx and ty > sy:
            if tx > ty:
                tx -= ty
            else:
                ty -= tx
        if tx == sx and ty >= sy:
            return ty % tx == sy % sx
        if tx >= sy and ty == sy:
            return tx % ty == sx % sy
        return False

sx = 3
sy = 7
tx = 3
ty = 4
s = Solution()
ans = s.reachingPoints(sx, sy, tx, ty)
print(ans)