"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    def find_sum(self, root):
        if root is None:
            return (0, 0)

        left = self.find_sum(root.left)
        right = self.find_sum(root.right)

        node_sum = root.val + left[0] + right[0]
        node_tile = abs(left[0] - right[0]) + left[1] + right[1]
        return (node_sum, node_tile)

    """
    @param root: the root
    @return: the tilt of the whole tree
    """

    def findTilt(self, root):

        # Write your code here
        if root is None:
            return 0

        return self.find_sum(root)[1]
