# Definition for a binary tree node.
class TreeNode:
    def __init__ (self, val=0, left=None, right=None):
       self.val = val
       self.left = left
       self.right = right

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(9)
root.left.left = TreeNode(1)
root.left.right = TreeNode(4)

val = 6


class Solution:
    def insertIntoBST(self, root, val: int):
        if not root:
            return TreeNode(val)

        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)

        return root

solution = Solution()
result = solution.insertIntoBST(root, val)
        

        