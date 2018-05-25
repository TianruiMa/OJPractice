"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param head: a ListNode
    @param val: An integer
    @return: a ListNode
    """

    def removeElements(self, head, val):
        # write your code here

        last_node = head
        current_node = head

        while current_node is not None:
            if current_node.val == val:
                if current_node is head:
                    head = current_node.next
                    current_node = head
                    last_node = head
                else:
                    last_node.next = current_node.next
                    current_node = current_node.next
                continue

            last_node = current_node
            current_node = current_node.next

        return head
