class Solution:
    def maximumSwap(self, num: 'int') -> 'int':
        N = str(num)
        for i in range(0, len(N)):
            nj = max(N[i+1:])
            if N[i] >= nj:
                continue
            for j in range(len(N)-1, i, -1):
                if N[j] == nj:
                    N = N[:i] + N[j] + N[i+1:j] + N[i] + N[j+1:]
                    return int(N)