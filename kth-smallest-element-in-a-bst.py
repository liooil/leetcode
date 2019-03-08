# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def countTree(self, node: TreeNode) -> int:
        if not node:
            return 0
        return 1 + self.countTree(node.left) + self.countTree(node.right)
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        L = self.countTree(root.left)
        if L == k-1:
            return root.val
        elif L > k-1:
            return self.kthSmallest(root.left, k)
        else:
            return self.kthSmallest(root.right, k-L-1)