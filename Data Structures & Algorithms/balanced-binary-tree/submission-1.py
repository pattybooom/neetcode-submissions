# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def heightOfSubtree(node):
            height = 1
            
            if node:
                if node.left and node.right:
                    left = heightOfSubtree(node.left)
                    right = heightOfSubtree(node.right)
                    

                    if not left or not right:
                        return False
                    diff = abs(left-right)

                    if diff <= 1:
                        return max(left,right) + 1
                    else:
                        return False
                elif node.left:
                    left = heightOfSubtree(node.left)
                    if not left:
                        return False
                    if left > 1:
                        return False
                    return left+1
                elif node.right:
                    right = heightOfSubtree(node.right)
                    if not right:
                        return False
                    if right > 1:
                        return False
                    return right+1
                else:
                    return 1
            else:
                return 0
        if not root:
            return True

        a = heightOfSubtree(root)
        if a:
            return True
        
        return False

                    
                    




        