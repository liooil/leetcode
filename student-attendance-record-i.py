class Solution:
    def checkRecord(self, s: str) -> bool:
        As, Ls = 0, 0
        for c in s:
            if c == 'A':
                As += 1
                Ls = 0
                if As == 2:
                    return False
            elif c == 'L':
                Ls += 1
                if Ls == 3:
                    return False
            else:
                Ls = 0
        return True