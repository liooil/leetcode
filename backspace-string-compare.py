class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def getChar(it, cnt=0):
            try:
                c = next(it)
            except StopIteration:
                return None
            if c == '#':
                return getChar(it, cnt+1)
            elif cnt:
                return getChar(it, cnt-1)
            else:
                return c
        itS, itT = reversed(S), reversed(T)
        while True:
            cs, ct = getChar(itS), getChar(itT)
            if cs != ct:
                return False
            if cs == None:
                return True
        
            

            
s = Solution()
ans = s.backspaceCompare("ab#c", "")
print(ans)