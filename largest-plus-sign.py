import collections
class Solution:
    def orderOfLargestPlusSign(self, N: 'int', mines: 'List[List[int]]') -> 'int':
        # def PlusTier(i, j, T):
        #     return not any(
        #         (ii == i and abs(j-jj) < T) or (jj == j and abs(i-ii) < T) for (ii, jj) in mines
        #     )
        # for T in range((N+1)//2, 0, -1):
        #     for i in range(T-1, N-T+1):
        #         for j in range(T-1, N-T+1):
        #             if PlusTier(i, j, T):
        #                 return T
        # return 0
        invalids = collections.defaultdict(set)
        for ii, jj in mines:
            for T in range(N):
                for i in ii-T, ii+T:
                    for j in jj-T, jj+T:
                        
