class NumArray:

    def __init__(self, nums: 'List[int]'):
        self.N = len(nums)
        sums = [nums]
        while len(sums[-1]) > 1:
            last = sums[-1]
            sums.append([a+b for a, b in zip(last[::2], last[1::2])])
        self.sums = sums

    def update(self, i: 'int', val: 'int') -> 'None':
        valDiff = val - self.sums[0][i]
        for layer in range(0, len(self.sums)):
            if i == len(self.sums[layer]):
                break
            self.sums[layer][i] += valDiff
            i >>= 1

    def sumRange(self, i: 'int', j: 'int') -> 'int':
        def getSum(i, j, layer):
            if i == j:
                return self.sums[layer][i]
            ans = 0
            if i % 2 == 1:
                ans -= self.sums[layer][i-1]
            if j % 2 == 0:
                ans += self.sums[layer][j]
            return ans + getSum(i>>1, (j-1)>>1, layer+1)
        return getSum(i, j, 0)


# Your NumArray object will be instantiated and called as such:
obj = NumArray([1,3,5,7,9])
print(obj.sumRange(1,2))
obj.update(1,2)
print(obj.sumRange(1,2))