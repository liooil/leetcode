class Solution:
    def cherryPickup(self, grid: 'List[List[int]]') -> 'int':
        # PATH_HALF = len(grid)+len(grid[0])-1
        # PATH_FULL = 2*PATH_HALF-1
        # cmax = 0
        # Paths = [(grid[0][0], ((0, 0),))]
        # while Paths:
        #     val, path = Paths.pop()
        #     if val - len(path) + 2*(len(grid)+len(grid[0]))-3 < cmax:
        #         continue
        #     if len(path) == PATH_FULL:
        #         cmax = max(cmax, val)
        #     else:
        #         u, v = path[-1]
        #         uvs = []
        #         if len(path) < PATH_HALF:
        #             if u+1 < len(grid):
        #                 uvs.append((u+1, v))
        #             if v+1 < len(grid[0]):
        #                 uvs.append((u, v+1))
        #         else:
        #             if u:
        #                 uvs.append((u-1, v))
        #             if v:
        #                 uvs.append((u, v-1))
        #         for uu, vv in uvs:
        #             valN = val
        #             if grid[uu][vv] == 1 and (uu, vv) not in path:
        #                 valN += 1
        #             if grid[uu][vv] != -1:
        #                 Paths.append((valN, path + ((uu, vv),)))
        # return cmax
        m, n = len(grid), len(grid[0])
        Cherries = {}
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    Cherries[(i, j)] = len(Cherries)
        CollectedList = [[frozenset()] for i in range(m) for j in range(n)]
        if (0, 0) in Cherries:
            cid = Cherries[(0, 0)] # Cherries[(0, 0)] = 0
            CollectedList[0][0][k] = [frozenset({cid})]
        for i in range(m):
            for j in range(n):
                if i:
                    CollectedList[i][j] = CollectedList[i-1][j]
                    if j:
                        # merge
                        for collects in CollectedList[i][j-1]:
                            # TODO
                elif j:
                    CollectedList[i][j] = CollectedList[i][j-1]
                
                if (i, j) in Cherries:
                    cid = Cherries[(i, j)]
                    for k in range(len(CollectedList[i][j])):
                        CollectedList[i][j][k] = CollectedList[i][j][k] | {cid}

        # Cherries = [[] for i in range(len(grid)) for j in range(len(grid[i]))]
        # if grid[0][0] == 1:
        #     Cherries[0][0] = frozenset([(0, 0)])
        # if grid[0][0] == -1:
        #     return 0
        # for i in range(len(grid)):
        #     for j in range(len(grid[i])):
        #         if grid[i][j] == -1:
        #             continue                
        #         if i and j:
        #             paths = Cherries[i-1][j], Cherries[i][j-1] # merge
        #         elif i:
        #             paths = Cherries[i-1][j]
        #         elif j:
        #             paths = Cherries[i][j-1]
        #         else:
        #             paths = []
                
        #         if grid[i][j] == 1:
        #             for pid in range(len(paths)):
        #                 paths[pid] = paths[pid] + (i)
        #             (i, j) # add to each path
                
        #         Cherries[i][j] = paths
