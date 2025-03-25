# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        def search(root: Optional[TreeNode],depth: int) -> int :
            if root is None :
                return 100000
            if root.left == None and root.right == None :
                return depth+1
            return min(search(root.left,depth),search(root.right,depth))+1

        return search(root,0)

        
