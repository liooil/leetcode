class Solution:
    def judgeCircle(self, moves: str) -> bool:
        D = {'U':0, 'D':0, 'L':0, 'R':0}
        for dir in moves:
            D[dir] += 1
        return D['U'] == D['D'] and D['L'] == D['R']