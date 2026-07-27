# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if not lists:
            return None
        
        heap = []

        for l in lists:
            t = l
            while t:

                heapq.heappush(heap, t.val)
                t = t.next
        
        dummy = ListNode(0)
        curr = dummy
        while heap:
            curr.next = ListNode(heapq.heappop(heap))
            curr = curr.next
        return dummy.next
