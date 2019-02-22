class Solution:
    def maxSumSubmatrix(self, matrix: 'List[List[int]]', k: 'int') -> 'int':
        m, n = len(matrix), len(matrix[0]) if matrix else 0
        # Frags = [
        #     [[matrix[i][j] for j in range(n)]] for i in range(m)
        # ]
        # for i in range(m):
        #     while len(Frags[i][-1]) > 1:
        #         Frags[i].append(
        #             [a+b for a, b in zip(Frags[i][-1][::2], Frags[i][-1][1::2])]
        #         )
        # def getIn(i, js, jt):
        #     if (i, js, jt) not in memo:
        #     ans = 0
        #     for layer in Frags[i]:
        #         if js == jt:
        #             ans += layer[js]
        #             break
        #         if js&1:
        #             js -= 1
        #             ans -= layer[js]
        #         if not jt&1:
        #             ans += layer[jt]
        #             jt -= 1
        #         js >>= 1
        #         jt >>= 1
        #     return ans
        memo = {}
        def getIn(i, js, jt):
            if js == jt:
                return matrix[i][js]
            if (i, js, jt) not in memo:
                memo[(i, js, jt)] = getIn(i, js, jt-1) + matrix[i][jt]
            return memo[(i, js, jt)]
        def getN():
            for js in range(n):
                for jt in range(js, n):
                    for i_s in range(m):
                        s = 0
                        for i_t in range(i_s, m):
                            s += getIn(i_t, js, jt)
                            if s <= k:
                                yield s
        return max(getN(), default=None)