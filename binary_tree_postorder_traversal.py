''' 145. Binary Tree Postorder Traversal

Given the root of a binary tree, return the postorder traversal of its nodes values.

Example:
    input = [1, null, 2, 3]
    output = [3, 2, 1]

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [root]
        visit = [False]
        result = []

        while stack:
           cur, v = stack.pop(), visit.pop()
           if cur:
               if v:
                   result.append(cur.val)
               else:
                   stack.append(cur)
                   visit.append(True)
                   stack.append(cur.right)
                   visit.append(False)
                   stack.append(cur.left)
                   visit.append(False)
        return result

