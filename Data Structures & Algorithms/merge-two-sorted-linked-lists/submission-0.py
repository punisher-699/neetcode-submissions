# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        l, ll = list1, list2
        if not l and not ll:
            return l
        if not l:
            return ll
        if not ll:
            return l
        
        nl = ListNode()
        fh = nl
        while l and ll:
            if l.val <= ll.val:
                nl.next = ListNode(l.val)
                
                l = l.next
            else:
                nl.next = ListNode(ll.val)
                ll = ll.next
            nl = nl.next
        while l:
            nl.next = ListNode(l.val)
            nl = nl.next
            l = l.next
        while ll:
            nl.next = ListNode(ll.val)
            nl = nl.next
            ll = ll.next
        return fh.next

           
