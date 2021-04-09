# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        elements = []
        
        if root.val == None:
            return False

        if root.left:
            # Check if not valid
            if root.val <= root.left.val:
                return False
            elements += self.isValidBST(root=root.left)

        elements.append(root.val)

        if root.right:
            # Check if not valid
            if root.val >= root.right.val:
                return False
            elements += self.isValidBST(root=root.right)
        
        return elements
