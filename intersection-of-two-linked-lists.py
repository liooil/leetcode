# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        def getLength(node):
            N = 0
            while node:
                node = node.next
                N += 1
            return N
        NA, NB = getLength(headA), getLength(headB)
        while NA > NB:
            headA = headA.next
            NA -= 1
        while NA < NB:
            headB = headB.next
            NB -= 1
        while headA != headB:
            headA = headA.next
            headB = headB.next
        return headA