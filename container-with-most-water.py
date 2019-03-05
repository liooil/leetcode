class Solution:
    def maxArea(self, height: 'List[int]') -> int:
        # Ls, Rs = [], []
        # for i in range(len(height)):
        #     if not Ls or height[i] > height[Ls[-1]]:
        #         Ls.append(i)
        # for j in reversed(range(len(height))):
        #     if not Rs or height[j] > height[Rs[-1]]:
        #         Rs.append(j)

        i, j = 0, len(height)-1
        HI, HJ = None, None
        ans = 0
        while i < j:
            hi, hj = height[i], height[j]

            if hi < hj:
                ans = max(ans, (j-i) * hi)
                for ii in range(i+1, j):
                    if HI == None or height[ii] > HI:
                        i = ii
                        HI = height[i]
                        break
                else:
                    break
            else:
                ans = max(ans, (j-i) * hj)
                for jj in range(j-1, i, -1):
                    if HJ == None or height[jj] > HJ:
                        j = jj
                        HJ = height[j]
                        break
                else:
                    break

        return ans

height = [1,8,6,2,5,4,8,3,7]
s = Solution()
ans = s.maxArea(height)
print(ans)