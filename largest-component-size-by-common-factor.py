import math, collections

class Solution:
    def factorize(self, n: 'int') -> 'Set[int]':
        out = set()
        while n % 2 == 0: 
            out.add(2)
            n //= 2
        for i in range(3, int(math.sqrt(n))+1, 2): 
            while n % i== 0: 
                out.add(i) 
                n //= i 
        if n > 2: 
            out.add(n)
        return out
    def getRoot(self, D: 'Dict[int->int]', d: 'int') -> 'int':
        if D[d] > 0:
            D[d] = self.getRoot(D, D[d])
            return D[d]
        else:
            return d
    def largestComponentSize(self, A: 'List[int]') -> 'int':
        Primes = [2]
        for i in range(3, 11412, 2):
            if all(i % p for p in Primes):
                Primes.append(i)
        print(Primes)
        D = collections.defaultdict(int)
        ans = 0
        for a in A:
            F = self.factorize(a)
            if F:
                d0 = self.getRoot(D, F.pop())
                D[d0] -= 1
                for f in F:
                    d = self.getRoot(D, f)
                    if d != d0:
                        D[d0] += D[d]
                        D[d] = d0
                ans = max(ans, -D[d0])
        return ans
        

A = [2,3,6,7,4,12,21,39]
s = Solution()
ans = s.largestComponentSize(A)
print(ans)