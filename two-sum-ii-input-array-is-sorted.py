class Solution:
    def twoSum(self, numbers: 'List[int]', target: 'int') -> 'List[int]':
        hi = len(numbers)-1
        for i in range(len(numbers)-1):
            lo = i+1
            while lo <= hi:
                j = (lo+hi)//2
                if numbers[i] + numbers[j] < target:
                    lo = j+1
                elif numbers[i] + numbers[j] > target:
                    hi = j-1
                else:
                    return i+1, j+1
