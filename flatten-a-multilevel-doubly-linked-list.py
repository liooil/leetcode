"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        def stick(nodeA, nodeB):
            if nodeA:
                nodeA.next = nodeB
            if nodeB:
                nodeB.prev = nodeA
        node = head
        while node:
            if node.child:
                child = node.child
                while child.next:
                    child = child.next
                stick(child, node.next)
                stick(node, child)
                node.child = None
            node = node.next
        return head
