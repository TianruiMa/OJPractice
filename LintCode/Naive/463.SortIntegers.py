class Solution:
    """
    @param A: an integer array
    @return: nothing
    @algorithm: bubble sort
    """

    def sortIntegers(self, A):
        # write your code here
        if A is None or len(A) < 2:
            return A
        current_index = 0
        while current_index < len(A) - 1:
            if A[current_index] > A[current_index + 1]:
                tmp = A[current_index]
                A[current_index] = A[current_index + 1]
                A[current_index + 1] = tmp
            current_index += 1

        res = self.sortIntegers(A[0:-1])
        res.append(A[-1])
        print(res)
        return res
