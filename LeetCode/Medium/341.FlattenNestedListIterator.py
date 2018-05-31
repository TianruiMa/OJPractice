# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    #     def __init__(self, nestedList):
    #         """
    #         Initialize your data structure here.
    #         :type nestedList: List[NestedInteger]
    #         """
    #         self.ind = 0
    #         self.my_list =[]
    #         for n in nestedList:
    #             self.my_list.extend(self.flatten(n))

    #     def flatten(self,nestedList):
    #         flatten_list = []
    #         if nestedList.isInteger():
    #             flatten_list.append(nestedList.getInteger())
    #         else:
    #             for l in nestedList.getList():
    #                 flatten_list.extend(self.flatten(l))
    #         return flatten_list

    #     def next(self):
    #         """
    #         :rtype: int
    #         """
    #         self.ind+=1
    #         return self.my_list[self.ind-1]

    #     def hasNext(self):
    #         """
    #         :rtype: bool
    #         """
    #         return self.ind < len(self.my_list)

    def __init__(self, nestedList):
        self.stack = [item for item in nestedList[::-1]]

    def next(self):
        return self.stack.pop().getInteger()

    def hasNext(self):
        while self.stack:
            if self.stack[-1].isInteger():
                return True
            curr = self.stack.pop()
            for item in curr.getList()[::-1]:
                self.stack.append(item)
        return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())