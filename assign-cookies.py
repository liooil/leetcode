class Solution:
    def findContentChildren(self, g: 'List[int]', s: 'List[int]') -> 'int':
        childiter = iter(sorted(g))
        cookieiter = iter(sorted(s))
        cnt = 0
        try:
            while True:
                child = next(childiter)
                cookie = next(cookieiter)
                while cookie < child:
                    cookie = next(cookieiter)
                cnt += 1
        except StopIteration:
            return cnt