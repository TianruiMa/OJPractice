"""
Definition of ListNode

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param head: n
    @return: The new head of reversed linked list.
    """

    def reverse(self, head):
        # write your code here

        last = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = last
            last = curr
            curr = next_node
            # curr, curr.next, last = curr.next, last, curr
        return last


a = ListNode(1)city
a.next = ListNode(2)
a.next.next = ListNode(3)

print (Solution().reverse(a))