# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return 

        def merge2Lists(l1, l2):
            if not l1:
                return l2
            if not l2:
                return l1
            current = ListNode()

            if l1.val <= l2.val:
                current = l1
                l1 = l1.next
                current.next = merge2Lists(l1,l2)
            else:
                current = l2
                l2 = l2.next
                current.next = merge2Lists(l1,l2)
            return current 
        
        def merge2Iter(l1, l2):
            dummy = ListNode()
            tail = dummy

            while l1 and l2:
                if l1.val <= l2.val:
                    tail.next = l1
                    l1 = l1.next 
                else:
                    tail.next = l2
                    l2 = l2.next 
                tail = tail.next
            if l1:
                tail.next = l1
            elif l2:
                tail.next = l2

            return dummy.next
        
        
        while len(lists) >= 2:
            sets = []
            while len(lists) >= 2:
                sets.append((lists.pop(), lists.pop()))
            for x in sets:
                lists.append(merge2Iter(x[0],x[1]))
                
        
        return lists[0]
        

        