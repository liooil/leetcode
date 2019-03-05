# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        itPre = iter(preorder)
        DIn = {x: i for i, x in enumerate(inorder)}
        def helper(L, R):
            if L < R:
                M = DIn[next(itPre)]
                root = TreeNode(inorder[M])
                root.left, root.right = helper(L, M), helper(M+1, R)
                return root
        
        return helper(0, len(preorder))