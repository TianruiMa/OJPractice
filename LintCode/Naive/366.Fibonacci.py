class Solution:
    """
    @param n: an integer
    @return: an ineger f(n)
    """

    def fibonacci(self, n):

        actual_index = n - 1

        fibonacci_list = [0, 1]

        if actual_index == 0: return 0
        if actual_index == 1: return 1

        for index in range(2, actual_index + 1):
            fibonacci_list.append(fibonacci_list[index - 1] + fibonacci_list[index - 2])

        return fibonacci_list[actual_index]


print Solution().fibonacci(10)
