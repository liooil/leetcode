# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import heapq

class Solution:
    def findSecondMinimumValue(self, root: 'TreeNode') -> 'int':
        def helper(node: 'TreeNode') -> 'int, int':
            if not node:
                return
            yield node.val
            yield from helper(node.left)
            yield from helper(node.right)
        heap = [-1, -1]
        for v in helper(root):
            if heap[0] == -1 or v <= heap[0]:
                heap[0] = v
            elif heap[1] == -1 or v < heap[1]:
                heap[1] = v
        return heap[1]