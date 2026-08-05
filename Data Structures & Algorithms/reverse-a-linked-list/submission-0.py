# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #recurse down to tail 
        if head:
            if head.next:
                #we have a next so we recurse until we at tail 
                newHead = self.reverseList(head.next)
                #newhead is the current node.next so we want prevnode.next to equal this node 
                head.next.next = head
                head.next = None
                return newHead
            else:
                #no next so we are at tail.
                #we return the node to layer above and make next the node of above layer 
                return head
        