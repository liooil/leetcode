class Solution:
    def countArrangement(self, N: 'int') -> 'int':
        valids = {i:set() for i in range(1, N+1)}
        for i in range(1, N+1):
            for j in range(1, i+1):
                if i%j == 0:
                    valids[i].add(j)
                    valids[j].add(i)
        def DFS(i, X):
            if i == 1:
                return 1
            return sum(
                DFS(i-1, X-{j}) for j in X & valids[i]
            )
            
        return DFS(N, set(range(1, N+1)))

if __name__ == "__main__":
    s = Solution()
    for i in range(1, 16):
        ans = s.countArrangement(i)
        print(i, ans)