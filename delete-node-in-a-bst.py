# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deleteNode(self, root: 'TreeNode', key: 'int') -> 'TreeNode':
        if not root:
            return
        if root.val == key:
            tail = root.left
            if tail:
                while tail.right:
                    tail = tail.right
                tail.right = root.right
                return root.left
            else:
                return root.right
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
            return root
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
            return root

