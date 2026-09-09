# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        if not head or not head.next:
            return

        length = 0
        temp = head

        while temp:
            length += 1
            temp = temp.next

        i = 0 
        temp = head

        while i < length // 2:
            i += 1
            temp = temp.next

        l2 = temp.next
        temp.next = None
        prev, curr = None, l2
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        t2 = prev
        
        t1 = head
        while t1 and t2:
           
            temp1 = t1.next
            temp2 = t2.next
            t1.next = t2
            t2.next = temp1
            t1 = temp1
            t2 = temp2
        

    
    
        