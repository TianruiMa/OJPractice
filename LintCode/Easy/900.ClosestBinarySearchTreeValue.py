"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """

    def closestValue(self, root, target):
        # write your code here

        if target == root.val:
            return root.val
        elif target < root.val:
            if root.left is None:
                return root.val
            closed_value = self.closestValue(root.left, target)
        elif target > root.val:
            if root.right is None:
                return root.val
            closed_value = self.closestValue(root.right, target)

        curr_diff = abs(root.val - target)
        child_diff = abs(closed_value - target)
        if curr_diff > child_diff:
            return closed_value
        else:
            return root.val
