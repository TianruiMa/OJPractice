class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_int = sys.maxint

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if x <= self.min_int:
            self.stack.append(self.min_int)
            self.min_int = x
        self.stack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if self.stack.pop() == self.min_int:
            self.min_int = self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_int