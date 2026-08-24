# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def search(node, count): 
            right = 0
            left = 0

            if node:
                if node.left:
                    left = search(node.left,1)
                if node.right:
                    right = search(node.right,1)
                
                print(f"node {node.val}: left = {left}, right = {right}")
            else:
                return 0
            
            self.res = max(self.res, left+right)
            return max(count,left+1,right+1) 

        search(root,0)
        return self.res


