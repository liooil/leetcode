class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        ans = set()
        xx = 1
        while xx < bound:
            yy = 1
            while xx + yy <= bound:
                ans.add(xx+yy)
                if y == 1:
                    break
                yy *= y
            if x == 1:
                break
            xx *= x
        return list(ans)