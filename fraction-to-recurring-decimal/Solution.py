class Solution:
    def fractionToDecimal(self, numerator: 'int', denominator: 'int') -> 'str':
        isNeg = numerator != 0 and (numerator < 0) != (denominator < 0)
        numerator, denominator = map(abs, (numerator, denominator))
        memo = {}
        n0, r = divmod(numerator, denominator)
        Ds = []
        DecPart, InfPart = "", ""
        while r:
            if r-1 in memo:
                InfIdx = memo[r-1]
                DecPart = '.'+ ''.join(Ds[:InfIdx])
                InfPart = '(' + ''.join(Ds[InfIdx:]) + ')'
                break
            memo[r-1] = len(Ds)
            n, r = divmod(r*10, denominator)
            Ds.append(str(n))
        else:
            DecPart = '.' + ''.join(Ds) if Ds else ''
        return "{sign}{IntPart}{DecPart}{InfPart}".format(
            sign='-' if isNeg else '',
            IntPart=str(n0),
            DecPart=DecPart,
            InfPart=InfPart
        )

if __name__ == "__main__":
    s = Solution()
    ans = s.fractionToDecimal(
        -96
        ,90
    )
    print(ans)