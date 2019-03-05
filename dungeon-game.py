import math
class Solution:
    def calculateMinimumHP(self, dungeon: 'List[List[int]]') -> int:
        n = len(dungeon[0]) if dungeon else 0
        Heals = [None for j in range(n)]
        for line in reversed(dungeon):
            for j in reversed(range(n)):
                Heals[j] = max(
                    min(
                        (heal for heal in Heals[j:j+2] if heal != None), default=1
                    ) - line[j],
                    1
                )
        return Heals[0]

dungeon = [
    [-2,-3,3],
    [-5,-10,1],
    [10,30,-5]
]
s = Solution()
ans = s.calculateMinimumHP(dungeon)
print(ans)