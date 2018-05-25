class Solution:
    """
    @param nums: an array
    @param k: an integer
    @return: the maximum average value
    """

    def findMaxAverage(self, nums, k):
        max_sum = 0
        new_sum = 0
        for it in range(0, k):
            max_sum += nums[it]
            new_sum += nums[it]

        for index in range(0, len(nums) - k):
            old_dig = nums[index]
            new_dig = nums[index + k]
            new_sum = new_sum - old_dig + new_dig
            if new_dig < old_dig:
                continue

            max_sum = max(max_sum, new_sum)

        return max_sum * 1.0 / k
