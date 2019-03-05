class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        ans = cnt = 0
        for i in range(len(nums)):
            if not i or nums[i] > nums[i-1]:
                cnt += 1
            else:
                ans = max(ans, cnt)
                cnt = 1
        return max(ans, cnt)