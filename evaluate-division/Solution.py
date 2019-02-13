class Solution:
    def calcEquation(self, equations: 'List[List[str]]', values: 'List[float]', queries: 'List[List[str]]') -> 'List[float]':
        Edges = {}
        for (a, b), k in zip(equations, values):
            if a not in Edges:
                Edges[a] = {}
            if b not in Edges:
                Edges[b] = {}
            Edges[a][b] = 1/k
            Edges[b][a] = k
        def query(a, b):
            if b not in Edges:
                return -1.0
            Table = set()
            stack = [(b, 1)]
            while stack:
                v, val = stack.pop()
                for u in Edges[v]:
                    if u == a:
                        return val * Edges[v][u]
                    if u in Table:
                        continue
                    stack.append((u, val * Edges[v][u]))
                    Table.add(u)
            return -1.0

        return [query(a, b) for a, b in queries]