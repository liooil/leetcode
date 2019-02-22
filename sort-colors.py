class Solution:
    def sortColors(self, nums: 'List[int]') -> 'None':
        """
        Do not return anything, modify nums in-place instead.
        """
        pointers = [-1]*3 # points to the end of a color
        for i in range(len(nums)):
            for color in reversed(range(nums[i],3)):
                pointers[color] += 1
                nums[pointers[color]] = color