class Solution:
    def numSubarrayProductLessThanK(self, nums: 'List[int]', k: 'int') -> 'int':
        s = 1
        left = 0
        ans = 0
        for right, n in enumerate(nums):
            s *= n
            while s >= k:
                if left == len(nums):
                    break
                s /= nums[left]
                left += 1
            else:
                ans += right-left+1
        return ans