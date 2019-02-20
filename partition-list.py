# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: 'ListNode', x: 'int') -> 'ListNode':
        LT, RT = LH, RH = ListNode(None), ListNode(None)
        while head:
            if head.val < x:
                LT.next = head
                LT = LT.next
            else:
                RT.next = head
                RT = RT.next
            head = head.next
        LT.next, RT.next = RH.next, None
        return LH.next