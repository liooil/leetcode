class Solution:
    def maxDistToClosest(self, seats: 'List[int]') -> 'int':
        ans = zeros = 0
        beg = True
        for s in seats:
            if s:
                ans = max(ans, zeros if beg else (zeros+1)//2)
                beg = False
                zeros = 0
            else:
                zeros += 1        
        return max(ans, zeros)
           