class Solution:
    def networkDelayTime(self, times: 'List[List[int]]', N: 'int', K: 'int') -> 'int':
        Nodes = [None]*N
        Edges = {u:{} for u in range(N)}
        for u, v, w in times:
            Edges[u-1][v-1] = w
        Nodes[K-1] = 0
        stack = [K-1]
        while stack:
            u = stack.pop()
            for v, w in Edges[u].items():
                if Nodes[v] == None or Nodes[v] > Nodes[u]+w:
                    Nodes[v] = Nodes[u]+w
                    stack.append(v)
        return -1 if None in Nodes else max(Nodes)

if __name__ == "__main__":
    s = Solution()
    ans = s.networkDelayTime(
        [[2,1,1],[2,3,1],[3,4,1]],
        4,
        2
    )
    print(ans)