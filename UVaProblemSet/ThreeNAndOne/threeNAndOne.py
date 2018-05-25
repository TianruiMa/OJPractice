from solution import solver
class ThreeNAndOne:

    def __init__(self):
        self.big_range = []
        self.range_array = []
        self.small = 0
        # count = 0

    def get_element_calculated(self,e):
        # global range_array
        # global small
        # global count
        if e in self.big_range:
            # if range_array[e - small] != -1:
            #     count += 1
            self.range_array[e - self.small] = -1
        result_list = [e]
        if e == 1:
            return result_list
        elif e % 2 == 0:
            e >>= 1
        else:
            e = e * 3 + 1
        result_list.extend(self.get_element_calculated(e))
        return result_list

    # def reset():
    #     big_range = []
    #     range_array = []
    #     small = 0

    def three_n_and_one(self,a, b):
        # global small
        small = min(a, b)
        large = max(a, b)
        # global big_range
        big_range = range(small, large + 1)

        # global range_array

        for index in range(small, large + 1):
            self.range_array.append(0)

        max_length = 0
        for position in range(0, large - small + 1):
            if self.range_array[position] != -1:
                real_num = position + small
                calculated_list = self.get_element_calculated(real_num)
                if max_length < len(calculated_list):
                    max_length = len(calculated_list)
        # reset()
        return max_length

    def test_cases(self):
        with open("TestCases.txt", "r") as inp:
            for line in inp:
                a, b, c = map(int, line.split())
                res = ThreeNAndOne.three_n_and_one(a, b)
                self.assertEqual(res, c)
        file.close(inp)

ans = True
with open("TestCases.txt", "r") as inp:
    for line in inp:
        a, b, c = map(int, line.split())
        res = solver(a, b)
        ans = ans and (res == c)
file.close(inp)
print(ans)