import math
class Solution:
    def shortestPathAllKeys(self, grid: 'List[str]') -> 'int':
        m, n = len(grid), len(grid[0])
        Keys = []
        Doors = []
        start = None
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '@':
                    start = (i, j)
                elif grid[i][j] in "abcdef":
                    id = ord(grid[i][j]) - ord('a')
                    if id >= len(Keys):
                        Keys.extend(None for _ in range(id-len(Keys)+1))
                    Keys[id] = (i, j)
                elif grid[i][j] in "ABCDEF":
                    id = ord(grid[i][j]) - ord('A')
                    if id >= len(Doors):
                        Doors.extend(None for _ in range(id-len(Doors)+1))
                    Doors[id] = (i, j)
        def BFS(pos0, targets):
            gridD = [[None]*n for _ in range(m)]
            gridD[pos0[0]][pos0[1]] = 0
            ans = [math.inf]*len(targets)
            queue = [pos0]
            d = 1
            while math.inf in ans and queue:
                queueN = []
                for i, j in queue:
                    for ii, jj in (i-1,j), (i+1,j), (i,j-1), (i,j+1):
                        if 0 <= ii < m and 0 <= jj < n:
                            if gridD[ii][jj] == None:
                                if (ii, jj) in targets:
                                    t_idx = targets.index((ii, jj))
                                    if ans[t_idx] == math.inf:
                                        ans[t_idx] = d
                                if grid[ii][jj] in '@.abcdef':
                                    gridD[ii][jj] = d
                                    queueN.append((ii,jj))
                queue = queueN
                d += 1
            return ans
        
        K = len(Keys)
        start2keys  = BFS(start, Keys)
        keys2keys   = [BFS(Keys[j], Keys[j+1:]) for j in range(K-1)]
        doors2doors = [BFS(Doors[j], Doors[j+1:]) for j in range(K-1)]
        keys2doors  = [BFS(Keys[i], Doors) for i in range(K)]
        print(start2keys)
        print(keys2keys)
        print(doors2doors)
        print(keys2doors)


        def getShortestPath(i, j, doors):
            i, j = sorted((i, j))
            D = [math.inf] * len(doors)
            ans = keys2keys[i][j-i-1]
            for did, d in enumerate(doors):
                D[did] = keys2doors[i][d]
            top = list(range(len(doors)))
            while top:
                topN = []
                for did in top:
                    if D[did] == math.inf:
                        continue
                    d = doors[did]
                    ans = min(ans, D[did] + keys2doors[j][d])
                    for did2 in range(len(doors)):
                        if did2 == did:
                            continue
                        ii, jj = sorted((doors[did], doors[did2]))
                        if D[did] + doors2doors[ii][jj-ii-1] < D[did2]:
                            D[did2] = D[did] + doors2doors[ii][jj-ii-1]
                            topN.append(did2)
                top = topN
            return ans

        ans = math.inf
        stack = [(tuple(), 0)]
        while stack:
            path, dis = stack.pop()
            print('->'.join(['@']+[chr(ord('a')+p) for p in path]), dis)
            if len(path) == K:
                ans = min(ans, dis)
            else:
                for i in range(K):
                    if i not in path:
                        if not path:
                            disN = dis + start2keys[i]
                        else:
                            disN = dis + getShortestPath(path[-1], i, path)
                        if disN < ans:
                            stack.append((path+(i,), disN))
        return ans if ans != math.inf else -1
        # to solve:
        # start -> key
        # key, door <-> key, door


if __name__ == "__main__":
    s = Solution()
    ans = s.shortestPathAllKeys(
        [
            "Dd#b@",
            ".fE.e",
            "##.B.",
            "#.cA.",
            "aF.#C"]
        )
    print(ans)