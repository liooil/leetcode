class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        N = len(row)//2
        Couples = [None for i in range(2*N)]
        for i in range(N):
            l, r = row[2*i:2*i+2]
            Couples[l] = r
            Couples[r] = l
        print(Couples)