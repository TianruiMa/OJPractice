class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        showed = [True] + [False]* len(nums)
        for x in nums:
            showed[x] = True
        return [i for i, y in enumerate(showed) if not y]