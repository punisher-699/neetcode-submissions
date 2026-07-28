# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        # def reverse(l):
        #     prev, curr, next = None, l, None;

        #     i = 1
        #     while (i <= k and curr):
        #         next = curr.next
        #         curr.next = prev
        #         prev = curr
        #         curr = next
        #     return prev
        # temp = head
        # head = reverse(temp)
        # i = 1
        # count = 1
        # while temp:
        #     count += 1
        #     i += 1
        #     if i % k == 0:
        #         temp.next = reverse(temp.next)
        #     temp = temp.next
        
        # if count % k != 0:
        #     i = 1
        #     temp = head
        #     while i < (count - (count % k)):
        #         temp = temp.next
        #     temp.next = reverse(temp.next)
        
        #return head

        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next

            prev, curr = groupNext, groupPrev.next
            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            temp = groupPrev.next
            groupPrev.next = kth
            groupPrev = temp
        
        return dummy.next

    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr

                
