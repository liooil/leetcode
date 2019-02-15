class Solution:
    def repeatedNTimes(self, A: 'List[int]') -> 'int':
        for i in range(4, len(A), 2):
            if A[i] == A[i+1]:
                return A[i]
        return A[3] if A[3] in A[1:3] else A[2] if A[2] in A[1:2] else A[0]

# class Solution:
#     def repeatedNTimes(self, A: 'List[int]') -> 'int':
#         for a, b in itertools.combinations(A[:4], 2):
#             if a == b:
#                 return a
#         for i in range(4, len(A), 2):
#             if A[i] == A[i+1]:
#                 return A[i]