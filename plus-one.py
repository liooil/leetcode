class Solution:
    def plusOne(self, digits: 'List[int]') -> 'List[int]':
        zeros = 0
        while digits:
            a = digits.pop()
            if a == 9:
                zeros += 1
            else:
                digits.append(a+1)
                break
        else:
            digits.append(1)
        digits.extend([0]*zeros)
        return digits