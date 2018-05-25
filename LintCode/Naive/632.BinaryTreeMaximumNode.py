"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: the root of tree
    @return: the max node
    """

    def maxNode(self, root):
        # write your code here

        if root is None:
            return None

        left_max = self.maxNode(root.left)
        right_max = self.maxNode(root.right)

        if left_max is None and right_max is None:
            return root
        elif left_max is None:
            return max(right_max, root, key=lambda x: x.val)
        elif right_max is None:
            return max(left_max, root, key=lambda x: x.val)
        else:
            return max(left_max, right_max, root, key=lambda x: x.val)
