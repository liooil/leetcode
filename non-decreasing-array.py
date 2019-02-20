class Solution:
    def checkPossibility(self, nums: 'List[int]') -> 'bool':
        invalids = [i for i in range(len(nums)-1) if nums[i] > nums[i+1]]
        if len(invalids) > 2:
            return False
        elif len(invalids) == 2:
            i, j = invalids
            if j != i+1:
                return False
            return nums[i] <= nums[i+2]
        elif len(invalids) == 1:
            i = invalids[0]
            if i==len(nums)-2 or nums[i] <= nums[i+2] or i==0 or nums[i-1] <= nums[i+1]:
                return True
            else:
                return False
        else:
            return True
        