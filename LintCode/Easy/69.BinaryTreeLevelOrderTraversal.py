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
    @return: Level order a list of lists of integer
    """

    # def bfs(self,root,level,queue):
    #     if root is None:
    #         return
    #     if level >= len(queue):
    #         queue.append([root.val])
    #     else:
    #         queue[level].append(root.val)
    #     self.bfs(root.left,level+1,queue)
    #     self.bfs(root.right,level+1,queue)

    def levelOrder(self, root):
        # write your code here
        #dfs
        trace_back = []
        my_list = []
        curr = root
        level = 0
        while True:
            if curr is None:
                if len(trace_back) == 0:
                    return my_list
                last_split = trace_back.pop()
                curr = last_split[0].right
                level = last_split[1]+1
            else:
                trace_back.append([curr,level])
                if level >= len(my_list):
                    my_list.append([curr.val])
                else:
                    my_list[level].append(curr.val)
                level += 1
                curr = curr.left

    #     my_queue = []
    #     self.bfs(root,0,my_queue)
    #     return my_queue





