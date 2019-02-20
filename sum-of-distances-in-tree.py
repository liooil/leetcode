class Solution:
    def sumOfDistancesInTree(self, N: 'int', edges: 'List[List[int]]') -> 'List[int]':
        Nodes = [None for i in range(N)]
        Edges = {i:{} for i in range(N)}
        for u, v in edges:
            Edges[u][v] = None
            Edges[v][u] = None
        # def getPoints(u, v):
        #     if Edges[u][v] == None:
        #         if Edges[v][u] == None:
        #             Edges[u][v] = 1 + sum(
        #                 getPoints(v, k) for k in Edges[v] if k != u
        #             )
        #             Edges[v][u] = N - Edges[u][v]
        #         else:
        #             Edges[u][v] = N - Edges[v][u]
        #     return Edges[u][v]
        def getLength(u, v):
            if Edges[u][v] == None:
                Edges[u][v] = (len(Edges[v])-1)*N + sum(
                    getLength(v, k) for k in Edges[v] if k != u
                )
            return Edges[u][v]
        Nodes[0] = 0
        stack = [0]
        while stack:
            u = stack.pop()
            for v in Edges[u]:
                if Nodes[v] == None:
                    Nodes[v] = Nodes[u] + Edges[u][v]
                    stack.append(v)
        return Nodes