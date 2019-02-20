"""
# Definition for a QuadTree node.
"""
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
class Solution:
    def construct(self, grid: 'List[List[int]]') -> 'Node':
        def helper(i, j, N):
            if N > 1:
                subs = [helper(ii, jj, N//2) for ii in (i, i+N//2) for jj in (j, j+N//2)]
                if any(not sub.isLeaf or sub.val != grid[i][j] for sub in subs):
                    return Node(None,False,subs[0],subs[1],subs[2],subs[3])
            return Node(grid[i][j],True,None,None,None,None)
        return helper(0, 0, len(grid))