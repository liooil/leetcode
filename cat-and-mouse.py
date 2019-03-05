class Solution:
    def catMouseGame(self, graph: 'List[List[int]]') -> int: # 0: DRAW, 1: MOUSE, 2: CAT
        N = len(graph)
        M = [[0 for _ in range(N)] for _ in range(N)] # Mouse's turn at M[m][c]
        C = [[0 for _ in range(N)] for _ in range(N)] # Cat's turn at C[m][c]
        for m in range(N):
            for c in range(N):
                if m == 0 or c == 0:
                    M[m][c] = C[m][c] = 1
                elif m == c:
                    M[m][c] = C[m][c] = 2
        while True:
            hasNew = False
            for m in range(N):
                for c in range(N):
                    if M[m][c] == 0:
                        # M[m][c] is 1 if any(children == 1)
                        if any(C[mN][c] == 1 for mN in graph[m]):
                            M[m][c] = 1
                            hasNew = True
                        # M[m][c] is 2 if all(children == 2)
                        elif all(C[mN][c] == 2 for mN in graph[m]):
                            M[m][c] = 2
                            hasNew = True
                    if C[m][c] == 0:
                        # C[m][c] is 1 if all(children == 1)
                        if any(M[m][cN] == 2 for cN in graph[c]):
                            C[m][c] = 2
                            hasNew = True
                        # C[m][c] is 2 if any(children == 2)
                        elif all(M[m][cN] == 1 for cN in graph[c]):
                            C[m][c] = 1
                            hasNew = True
            if M[1][2]:
                return M[1][2]
            elif not hasNew:
                return 0
        # print(G)

s = Solution()
ans = s.catMouseGame(
    [[1,3],[0],[3],[0,2]]
)
print(ans)