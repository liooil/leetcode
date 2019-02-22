class Solution:
    def findAnagrams(self, s: 'str', p: 'str') -> 'List[int]':
        cnt0 = {}
        for c in p:
            if c not in cnt0:
                cnt0[c] = 0
            cnt0[c] += 1
        cnti = {}
        for c in s[:len(p)]:
            if c not in cnti:
                cnti[c] = 0
            cnti[c] += 1
        ans = []
        if cnti == cnt0:
            ans.append(0)
        for i in range(len(s)-len(p)):
            j = i+len(p)
            cnti[s[i]] -= 1
            if cnti[s[i]] == 0:
                del cnti[s[i]]
            if s[j] not in cnti:
                cnti[s[j]] = 0
            cnti[s[j]] += 1
            if cnti == cnt0:
                ans.append(i+1)
        return ans