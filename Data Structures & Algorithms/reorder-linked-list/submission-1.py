# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        def recurseReorder(head):
            tail = head
            previous= ListNode()

            if head:
                while tail.next:
                    #getting last and second to last element
                    previous = tail
                    tail = tail.next

                if head.next == tail:
                    #if we just have two values e.g. [4,6]
                    return head

                nextN = head.next #recurse on next value 
                head.next = tail 
                
                previous.next = None
                tail.next = recurseReorder(nextN)
                
            return head

        recurseReorder(head)


       
        
        
       
           

        

           

            
            
            
            
        


