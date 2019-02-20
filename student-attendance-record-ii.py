import collections
class Solution1:
    def checkRecord(self, n: 'int') -> 'int':
        NN = collections.deque([0,1,1],maxlen=3) # without A  NLL,NL,N -,L,P
        NA = collections.deque([0,0,1],maxlen=3) # with A     NLL,NL,N -,-,A
        for _ in range(n):
            SN = sum(NN)%1000000007
            SA = (SN + sum(NA))%1000000007
            NN.append(SN)
            NA.append(SA)
        return NA[-1]

class Solution2:
    def checkRecord(self, n: 'int') -> 'int':
        vec = [0,1,1,0,0,1] # -,L,P;-,-,A; ~ [-,A][LL,L,-]
        def product6(matA, matB):
            return [[sum(
                        a*b%1000000007 for a, b in zip(matA[i], (matB[k][j] for k in range(6)))
                    ) for j in range(6)] for i in range(6)]
        def power6(mat, n):
            ans = [[i==j for j in range(6)] for i in range(6)]
            while n:
                if n & 1:
                    ans = product6(mat, ans)
                n >>= 1
                mat = product6(mat, mat)
            return ans
        mat0 = [
            [0,1,0,0,0,0], # NN[0] <= NN[1]
            [0,0,1,0,0,0], # NN[1] <= NN[2]
            [1,1,1,0,0,0], # NN[2] <= NN[:3]
            [0,0,0,0,1,0], # NN[3] <= NN[4]
            [0,0,0,0,0,1], # NN[4] <= NN[5]
            [1,1,1,1,1,1]  # NN[5] <= NN[:]
        ]
        return sum(a*b for a,b in zip(power6(mat0, n)[-1], vec))%1000000007

class Solution3:
    def checkRecord(self, n: 'int') -> 'int':
        class IntSqrt5:
            def __init__(self, x, y):
                self.x = x
                self.y = y
            def __mul__(self, other):
                xx, yy = other.x, other.y
                return IntSqrt5(self.x*xx+5*self.y*yy, self.x*yy+xx*self.y)
            def __pow__(self, n):
                ans = IntSqrt5(1,0)
                while n:
                    if n & 1:
                        ans *= self
                    n >>= 1
                    self = self * self
                return ans
        n = n + 1
        a = (1 + 5**0.5) / 4
        b = (1 - 5**0.5) / 4
        res = 2**n / 5**0.5 * ((1 - a**n) / (1 - a) * a - (1 - b**n) / (1 - b) * b)
        return res

s = Solution3()
a = s.checkRecord(5)