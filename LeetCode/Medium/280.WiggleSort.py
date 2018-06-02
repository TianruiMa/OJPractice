class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # Ture: <=
        # False: >=
        # comp_flag = True
        #
        # for index in range(len(nums) - 1):
        #     if comp_flag and nums[index] > nums[index + 1]:
        #         nums[index], nums[index + 1] = nums[index + 1], nums[index]
        #     elif (not comp_flag) and nums[index] < nums[index + 1]:
        #         nums[index], nums[index + 1] = nums[index + 1], nums[index]
        #     comp_flag = not comp_flag

        if not nums:
            return

        for i in range(1, len(nums), 2):
            if nums[i] < nums[i - 1]:
                nums[i - 1], nums[i] = nums[i], nums[i - 1]
            if i < len(nums) - 1 and nums[i] < nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]

