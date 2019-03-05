class Solution:
    def search(self, nums: 'List[int]', target: int) -> int:
        L, H = 0, len(nums)
        while L < H:
            M = (L+H) // 2
            if nums[M] < nums[0] < target: # +inf
                H = M
            elif nums[M] >= nums[0] > target: # -inf
                L = M+1
            elif nums[M] < target:
                L = M+1
            elif nums[M] > target:
                H = M
            else:
                return M
        return -1


nums = [3, 1]
target = 3

s = Solution()
ans = s.search(nums, target)
print(ans)