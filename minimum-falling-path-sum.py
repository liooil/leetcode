class Solution:
    def minFallingPathSum(self, A: 'List[List[int]]') -> 'int':
        accum = [0] * len(A[0])
        for line in A:
            accum = [d + min(
                accum[max(0, i-1):min(len(line), i+2)]
            ) for i, d in enumerate(line)]
        return min(accum)