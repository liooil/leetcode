class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        for i in range((len(B)-1)//len(A)+1, (len(B)+1)//len(A)+3):
            if B in i*A:
                return i
        return -1