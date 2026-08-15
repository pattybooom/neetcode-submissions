# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: 
        Optional[ListNode]) -> Optional[ListNode]:

        
        def addNodes(l1,l2,carry):
            
            if l1 and l2:
                Sum = l1.val + l2.val + carry
                
                if Sum > 9:
                    carry = 1
                    Sum = Sum - 10
                
                else:
                    carry = 0
            print(f"adding {l1.val} and {l2.val} = {Sum} carry {carry}")

            if l1.next and l2.next:
                node = ListNode(Sum, addNodes(l1.next,l2.next,carry))
                return node
            
            elif l1.next:
                
                carryNode = ListNode(carry)
                node = ListNode(Sum, addNodes(l1.next,carryNode,0))
                return node

            elif l2.next:
                carryNode = ListNode(carry)
                node = ListNode(Sum, addNodes(l2.next,carryNode,0))
                return node

            else:
                if carry:
                    node = ListNode(Sum,ListNode(1))
                    return node
                else:
                    node = ListNode(Sum)
                    return node


        return addNodes(l1,l2,0)
            

                    
        
        