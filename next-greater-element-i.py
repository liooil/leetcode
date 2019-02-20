class Solution:
    def nextGreaterElement(self, nums1: 'List[int]', nums2: 'List[int]') -> 'List[int]':
        Nexts = {n: -1 for n in nums1}
        L = set()
        for n in nums2:
            for l in frozenset(L):
                if l < n:
                    Nexts[l] = n
                    L.remove(l)
            if n in Nexts:
                L.add(n)
        return [Nexts[n] for n in nums1]
