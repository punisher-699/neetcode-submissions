"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        copylist = {None : None}

        curr = head
        while curr:
            new_node = Node(curr.val)
            copylist[curr] = new_node
            curr = curr.next

        curr = head
        while curr:
            temp = copylist[curr]
            temp.next = copylist[curr.next]
            temp.random = copylist[curr.random]
            curr = curr.next
        return copylist[head]




