# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        def recurseRemove(headNode):
            nonlocal n
            if headNode.next:
                recurseRemove(headNode.next)
            
            n -= 1
            if n == -1:
                headNode.next = headNode.next.next
            
        
        recurseRemove(head)
        if n == 0:
            print("ok")
            if not head.next:
                head = None
            else:
                head = head.next

        return head

     





        


        