class Solution(object):

    # @param nestedList a list, each element in the list
    # can be a list or integer, for example [1,2,[1,2]]
    # @return {int[]} a list of integer
    def flatten(self, nestedList):
        # Write your code here
        # stack = [x for x in nestedList[::-1]]
        if isinstance(nestedList, int): return [nestedList]
        # res = []

        # while nestedList:
        #     curr = nestedList.pop()
        #     if isinstance(curr,int):
        #         res.insert(0,curr)
        #     else:
        #         nestedList.extend(curr)
        # return res

        length = len(nestedList)
        index = 0

        while index < length:
            if isinstance(nestedList[index], int):
                index+=1
            else:
                length += len(nestedList[index])-1
                nestedList[index:index+1] = nestedList[index]
                # length = len(nestedList)
        return nestedList


a = [[1,2],3,[4,5]]
print(Solution().flatten(a))