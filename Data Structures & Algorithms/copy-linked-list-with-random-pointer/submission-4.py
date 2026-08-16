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
        copySet = {}
    
        curr = head
        while curr:
            copySet[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            if curr.next:
                copySet[curr].next = copySet[curr.next]
            if curr.random:
                copySet[curr].random = copySet[curr.random]
            curr = curr.next

        if head:
            return copySet[head]

        return 


        
