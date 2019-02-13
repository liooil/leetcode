class Solution:
    def removeKdigits(self, num: 'str', k: 'int') -> 'str':
        i = 0
        while k > 0 and i < len(num)-1:
            if num[i] > num[i+1]:
                num = num[:i]+num[i+1:]
                k -= 1
                if i > 0:
                    i -= 1
            else:
                i += 1
        if k:
            num = num[:-k]
        while num and num[0] == '0':
            num = num[1:]
        return num if num else '0'

if __name__ == "__main__":
    s = Solution()
    ans = s.removeKdigits(
        "12345"
        ,0
    )
    print(ans)