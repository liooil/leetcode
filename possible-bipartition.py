class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        Edges = {}
        for a, b in dislikes:
            if a not in Edges:
                Edges[a] = []
            if b not in Edges:
                Edges[b] = []
            Edges[a].append(b)
            Edges[b].append(a)
        Nodes = [None]*N

        while True:
            for i in range(N):
                if Nodes[i] == None:
                    stack = [i+1]
                    Nodes[i] = True
                    break
            else:
                break
            while stack:
                node = stack.pop()
                if node in Edges:
                    for child in Edges[node]:
                        if Nodes[child-1] == None:
                            Nodes[child-1] = not Nodes[node-1]
                            stack.append(child)
                        elif Nodes[child-1] == Nodes[node-1]:
                            return False
        return True
        