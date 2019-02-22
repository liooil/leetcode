# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findSecondMinimumValue(self, root: 'TreeNode') -> 'int':
        def helper(node: 'TreeNode') -> 'int, int':
            if not node:
                return -1, -1
            if not node.left:
                return node.val, -1
            smallest0, smallest1 = root.val, -1
            for v in helper(node.left) + helper(node.right):
                if v == -1:
                    continue
                if smallest0 == -1 or v < smallest0:
                    smallest0 = v
                elif smallest1 == -1 or v < smallest1:
                    smallest1 = v            
            return smallest0, smallest1
        _, ans = helper(root)
        return ans