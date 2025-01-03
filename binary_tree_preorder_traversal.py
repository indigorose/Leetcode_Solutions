''' 144. Binary Tree Preorder Traversal

Its considered easier to look at this recursively, but this will look at it iteratively.

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        current, stack = root, []
        result = []

        while current or stack:
            if current:
                result.append(current.val)
                stack.append(current.right)
                current = current.left
            else:
                current = stack.pop()

        return result
