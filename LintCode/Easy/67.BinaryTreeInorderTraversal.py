"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """

    def inorderTraversal(self, root):
        # write your code here

        node_list = []
        trace_back = []

        current = root
        insert_index = 0

        while True:
            if current is None:
                if len(trace_back) == 0:
                    return map(lambda x: x.val, node_list)
                last_split_node = trace_back.pop(-1)
                current = last_split_node.right
                insert_index = node_list.index(last_split_node) + 1
            else:
                trace_back.append(current)
                node_list.insert(insert_index, current)
                current = current.left
