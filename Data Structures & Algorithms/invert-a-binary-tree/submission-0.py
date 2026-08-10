# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            if root.left and root.right:
                print(f"root is {root.val}, left is {root.left.val} right is {root.right.val}")
            self.invertTree(root.left)
            self.invertTree(root.right)
            placeholder = root.left 
            root.left = root.right
            root.right = placeholder

            

            return root

        