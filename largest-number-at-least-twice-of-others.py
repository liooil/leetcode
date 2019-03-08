class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 1:
            return 0
        i0, i1 = heapq.nlargest(2, range(N), key=nums.__getitem__)
        if nums[i0] >= 2*nums[i1]:
            return i0
        else:
            return -1