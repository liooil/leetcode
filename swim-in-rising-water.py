import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        Children = [[] for i in range(N*N)]
        for x in range(N):
            for y in range(N):
                if x:
                    if grid[x-1][y] < grid[x][y]:
                        Children[grid[x][y]].append(grid[x-1][y])
                    else:
                        Children[grid[x-1][y]].append(grid[x][y])
                if y:
                    if grid[x][y-1] < grid[x][y]:
                        Children[grid[x][y]].append(grid[x][y-1])
                    else:
                        Children[grid[x][y-1]].append(grid[x][y])

        Groups = [i for i in range(N*N)]
        def getGroup(i):
            if Groups[i] == i:
                return i
            Groups[i] = getGroup(Groups[i])
            return Groups[i]
        def UnionGroup(i, j):
            i0, j0 = getGroup(i), getGroup(j)
            if i0 != j0:
                Groups[j0] = i0
        for t in range(N*N-1):
            for child in Children[t]:
                UnionGroup(child, t)
            if getGroup(grid[0][0]) == getGroup(grid[-1][-1]):
                return t
        return N*N-1