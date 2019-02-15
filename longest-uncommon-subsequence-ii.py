class Solution:
    def findLUSlength(self, strs: 'List[str]') -> 'int':
        def subseq(w1, w2):
            #True iff word1 is a subsequence of word2.
            i = 0
            for c in w2:
                if i < len(w1) and w1[i] == c:
                    i += 1
            return i == len(w1)
    
        strs.sort(key = len, reverse = True)
        for i, word1 in enumerate(strs):
            for j, word2 in enumerate(strs):
                if i == j:
                    continue
                if subseq(word1, word2):
                    break
            else:
                return len(word1)
        return -1