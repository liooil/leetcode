import bisect
class Solution:
    def threeSumClosest(self, nums: 'List[int]', target: int) -> int:
        nums.sort()
        N = len(nums)
        ans = sum(nums[:3])
        for k in range(2, N):
            i, j = 0, k-1
            while i < j:
                s = nums[i]+nums[j]+nums[k]
                ans = min((ans, s), key=lambda x: abs(x-target))
                if s < target:
                    i += 1
                elif s > target:
                    j -= 1
                else:
                    return s
        return ans

nums = [0,0,0]
target = 1
s = Solution()
ans = s.threeSumClosest(nums, target)
