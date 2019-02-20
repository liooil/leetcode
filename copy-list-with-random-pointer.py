# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        old2new = {}
        nodeN = None
        node = head
        while node:
            if nodeN:
                nodeN.next = RandomListNode(node.label)
                nodeN = nodeN.next
            else:
                nodeN = RandomListNode(node.label)
            old2new[node] = nodeN
            node = node.next
        node = head
        while node:
            nodeN = old2new[node]
            if node.random:
                nodeN.random = old2new[node.random]
            node = node.next
        return old2new[head]