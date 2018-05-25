class Solution:
    """
    @param ops: the list of operations
    @return:  the sum of the points you could get in all the rounds
    """

    def calPoints(self, ops):
        # Write your code here
        op_list = []
        my_sum = 0
        for op in ops:
            if op == "C":
                my_sum -= op_list.pop()
                continue
            elif op == "D":
                val = op_list[-1] * 2
            elif op == "+":
                val = op_list[-2] + op_list[-1]
            else:
                val = int(op)
            my_sum += val
            op_list.append(val)
        return my_sum
