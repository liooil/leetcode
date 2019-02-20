import itertools
class Solution:
    # def permute(self, nums: 'List[int]') -> 'List[List[int]]':
    #     # return list(itertools.permutations(nums))
    #     queue = []
    #     stack = [tuple()]
    #     while stack:
    #         path = stack.pop()
    #         if len(path) == len(nums):
    #             queue.append(list(path))
    #         else:
    #             for n in nums:
    #                 if n not in path:
    #                     stack.append(path+(n,))
    #     return queue
    permute = lambda nums: map(list, itertools.permutations(nums))