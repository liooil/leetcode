class Solution:
    def findDisappearedNumbers(self, nums: 'List[int]') -> 'List[int]':
        return list(
            frozenset(range(1, len(nums)+1)).difference(nums)
        )