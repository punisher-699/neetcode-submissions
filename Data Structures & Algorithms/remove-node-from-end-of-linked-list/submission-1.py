# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        length = 0
        temp = head
        while temp:
            temp = temp.next
            length += 1
        i = 1
        temp = head
        while i < (length - n ):
            i += 1
            temp = temp.next
        if temp.next != None:
            temp.next = temp.next.next
        else: temp.next = None
        return head
        