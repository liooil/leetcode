class Solution:
    def addToArrayForm(self, A: 'List[int]', K: 'int') -> 'List[int]':
        B = []
        while K:
            a = A.pop() if A else 0
            K += a
            K, r = divmod(K, 10)
            B.append(r)
        B.reverse()
        return A+B