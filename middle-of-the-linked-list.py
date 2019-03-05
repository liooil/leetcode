# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        tail, middle = head, head
        while True:
            if tail == None:
                break
            tail = tail.next
            if tail == None:
                break
            tail = tail.next
            middle = middle.next
        return middle