import collections, heapq
class Solution:
    def topKFrequent(self, words: 'List[str]', k: 'int') -> 'List[str]':
        Freqs = collections.Counter(words)
        return heapq.nsmallest(k, Freqs,
            key=lambda word:(~Freqs[word], word)
        )