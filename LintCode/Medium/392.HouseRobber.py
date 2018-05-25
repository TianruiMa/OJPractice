class Solution:
    """
    @param A: An array of non-negative integers
    @return: The maximum amount of money you can rob tonight
    """

    def houseRobber(self, A):
        index = 0
        last_one_sum = 0
        last_two_sum = 0
        last_three_sum = 0
        while index < len(A):
            tmp = last_one_sum
            last_one_sum = max(last_two_sum, last_three_sum) + A[index]
            last_three_sum = last_two_sum
            last_two_sum = tmp
            index += 1
        return max(last_one_sum, last_two_sum)
