# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #return root left right then left's left right and right left right 

        queue = []
        queue.append([root,0])
        output = []
        level = 0

        lev = {}

        while queue:
            node = queue[0][0]
            level = queue[0][1]

            if node:
                if node.left:
                    queue.append([node.left,level+1])
                if node.right:
                    queue.append([node.right,level +1])
            
                if level in lev:
                    lev[level].append(node.val)
                else:
                    lev[level] = [node.val]
            queue.remove(queue[0])

        for l in lev:
            output.append(lev[l])
        

        return output
        