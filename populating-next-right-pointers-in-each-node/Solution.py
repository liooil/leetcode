# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        start = root
        if not start:
            return
        start.next = None
        startN = start.left
        while startN:
            node, nodeN = start, startN
            while True:
                nodeN.next = node.right
                nodeN = nodeN.next
                node = node.next
                if not node:
                    nodeN.next = None
                    break
                nodeN.next = node.left
                nodeN = nodeN.next
            start, startN = startN, startN.left
