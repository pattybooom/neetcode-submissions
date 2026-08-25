# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.candidates = []


        def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            def checkNodes(n1, n2):
                if not n1 and not n2:
                    return True
                if not n1:
                    return False
                if not n2:
                    return False 

                if n1.val == n2.val:
                    if checkNodes(n1.left,n2.left):
                        if checkNodes(n1.right, n2.right):
                            return True
                
                return False

            return checkNodes(p,q)

        def traverse(node, val):
            if not node:
                return 

            left = None
            right = None

            if node.val == val:
                self.candidates.append(node)
            
            traverse(node.left, val)
            traverse(node.right, val)

            return


        node = traverse(root, subRoot.val)
        for x in self.candidates:
            if isSameTree(self, x, subRoot):
                return True
        return False
      

                









        