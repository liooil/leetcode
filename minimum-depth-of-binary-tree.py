# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: 'TreeNode') -> 'int':
        if not root:
            return 0
        def getChildren(node):
            children = [child for child in (node.left, node.right) if child]
            if children:
                return children
            raise ValueError
        depth = 0
        line = [root]
        while line:
            depth += 1
            try:
                line = [child for node in line for child in getChildren(node)]
            except ValueError:
                return depth