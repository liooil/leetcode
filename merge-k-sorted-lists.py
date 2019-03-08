# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

import heapq

class Solution:
    def mergeKLists(self, lists: 'List[ListNode]') -> ListNode:
        heap = [(node.val, i) for (i, node) in enumerate(lists) if node]
        if not heap:
            return None
        heapq.heapify(heap)
        node = dummy = ListNode(None)
        while heap:
            _, i = heapq.heappop(heap)
            node.next = lists[i]
            node = node.next
            lists[i] = lists[i].next
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i))
        return dummy.next