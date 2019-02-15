class Solution:
    def getRow(self, rowIndex: 'int') -> 'List[int]':
        DP = [1]
        for _ in range(rowIndex):
            DP = [1] + [x+y for x, y in zip(DP[1:], DP[:-1])] + [1]
        return DP