import heapq
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __lt__(self, other):
        return self.val < other.val


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        min_heap = []
        for node in lists:
            heapq.heappush(min_heap, node)

        start = None
        current = None
        while min_heap:
            node = heapq.heappop(min_heap)
            if node.next:
                heapq.heappush(min_heap, node.next)
            if not start:
                start = node
                current = node
            else:
                current.next = node
                current=node
            node.next=None

        return start


[[1, 4, 5], [1, 3, 4], [2, 6]]

node1 = ListNode(1, ListNode(4, ListNode(5, None)))
node2 = ListNode(1, ListNode(3, ListNode(4, None)))
node3 = ListNode(2, ListNode(6, None))
Solution().mergeKLists([node1, node2, node3])
