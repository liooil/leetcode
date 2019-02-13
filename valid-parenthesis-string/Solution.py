class Solution:
    def checkValidString(self, s: 'str') -> 'bool':
        degreeL, degreeH = 0, 0
        for c in s:
            if c == '(':
                degreeL += 1
                degreeH += 1
            elif c == ')':
                if degreeL > 0:
                    degreeL -= 1
                if degreeH > 0:
                    degreeH -= 1
                else:
                    return False
            else:
                if degreeL > 0:
                    degreeL -= 1
                degreeH += 1
        return degreeL == 0

if __name__ == "__main__":
    s = Solution()
    ans = s.checkValidString(
        "(())((())()()(*)(*()(())())())()()((()())((()))(*"
    )
    print(ans)