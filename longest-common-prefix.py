class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        ref = strs.pop()
        for i in range(len(ref)):
            for st in strs:
                if i == len(st) or st[i] != ref[i]:
                    return ref[:i]
        return ref