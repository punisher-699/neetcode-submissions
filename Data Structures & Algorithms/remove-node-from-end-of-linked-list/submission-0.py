# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        length = 0
        temp = head
        while temp:
            temp = temp.next
            length += 1
        i = 1
        temp = head
        while i < (length - n + 1):
            i += 1
            temp = temp.next
        temp.next = temp.next.next
        return head
        