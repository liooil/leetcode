class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        def goDir(pos, dir):
            while True:
                for d in range(2):
                    pos[d] += dir[d]
                if all(0 <= pos[d] < 8 for d in range(2)):
                    if board[pos[0]][pos[1]] == 'p':
                        return 1
                    elif board[pos[0]][pos[1]] == 'B':
                        return 0
                else:
                    return 0
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    return sum(
                        goDir([i, j], dir) for dir in [(-1, 0), (1, 0), (0, -1), (0, 1)]
                    )