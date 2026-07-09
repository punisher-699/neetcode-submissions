# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        length = 0

        temp = head
        while temp:
            length += 1
            temp = temp.next

        stack = []
        temp = head
        i = 0
        while i < length // 2:
            i += 1
            temp = temp.next
        l2 = temp.next
        temp.next = None
        temp = l2
        while temp:
            stack.append(temp)
            temp = temp.next
        
        temp = head
        while stack:
            tempt = temp.next
            temp.next = stack.pop()
            temp.next.next = tempt
            temp = tempt

            
        

        
        
