class Solution:
    def combine(self, n: 'int', k: 'int') -> 'List[List[int]]':
        queue = []
        stack = [tuple()]
        while stack:
            path = stack.pop()
            if 0 < len(path) < k:
                for i in range(path[-1]+1, n+1):
                    stack.append(path+(i,))
            elif len(path) == k:
                queue.append(path)
            else:
                for i in range(1, n+1):
                    stack.append(path+(i,))
        return queue