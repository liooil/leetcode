import heapq

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        Ls, Rs = [], []
        for n in nums:
            if Ls and n > ~Ls[0]:
                if len(Rs) == len(Ls):
                    heapq.heappush(Ls, ~heapq.heappushpop(Rs, n))
                else:
                    heapq.heappush(Rs, n)
            else:
                if len(Ls) == len(Rs)+1:
                    heapq.heappush(Rs, ~heapq.heappushpop(Ls, ~n))
                else:
                    heapq.heappush(Ls, ~n)
        return sum(l - Ls[0] for l in Ls[1:]) + sum(r - ~Ls[0] for r in Rs)