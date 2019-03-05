# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        Sums = []
        stack = [(root, 0)]
        while stack:
            node, level = stack.pop()
            if node:
                if level == len(Sums):
                    Sums.append([0, 0])
                Sums[level][0] += node.val
                Sums[level][1] += 1
                stack.append((node.left, level+1))
                stack.append((node.right, level+1))
        return [s/n for s, n in Sums]