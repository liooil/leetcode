# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDiffInBST(self, root: 'TreeNode') -> 'int':
        def helper(node: 'TreeNode', l: 'int', r: 'int'):
            ansL = []
            if node.left:
                ansL.append(helper(node.left, l, node.val))
            elif l != None:
                ansL.append(node.val-l)
            if node.right:
                ansL.append(helper(node.right, node.val, r))
            elif r != None:
                ansL.append(r-node.val)
            return min(ansL)
        return helper(root, None, None)
            