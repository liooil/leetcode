class Solution:
    def canIWin(self, maxChoosableInteger: 'int', desiredTotal: 'int') -> 'bool':
        memo = {}
        def canWin(desiredRemain: 'int', X: 'tuple'):
            if X[-1] >= desiredRemain:
                return True
            if X not in memo:
                memo[X] = not all(
                    canWin(desiredRemain-X[i], X[:i]+X[i+1:]) for i in range(len(X))
                )
            return memo[X]
        if desiredTotal > sum(range(1,maxChoosableInteger+1)):
            return False
        return canWin(desiredTotal, tuple(range(1, maxChoosableInteger+1)))