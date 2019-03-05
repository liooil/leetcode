class Solution:
    def threeSumMulti(self, A: List[int], target: int) -> int:
        D = [0 for a in range(101)]
        for a in A:
            D[a] += 1
        
        def getTuples(D):
            for i in range(101):
                if D[i] == 0:
                    continue
                if i + i + i == target:
                    yield D[i] * (D[i] - 1) * (D[i] - 2) //3//2
                for j in range(i+1, 101):
                    if D[j] == 0:
                        continue
                    if i + j + j == target:
                        yield D[i] * D[j] * (D[j] - 1) //2
                    if i + i + j == target:
                        yield D[i] * (D[i]-1) * D[j] //2
                    k = target - i - j
                    if j < k < 101:
                        yield D[i] * D[j] * D[k]
        ans = 0
        for t in getTuples(D):
            ans = (ans + t) % 1000000007
        return ans