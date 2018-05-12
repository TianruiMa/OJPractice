import sys


class EcologicalBinPacking:

    def __init__(self):
        self.permutation_list = []
        self.cost_list = []

    def permutations(self, head, tail=''):
        if len(head) == 0:
            self.permutation_list.append(tail)
        else:
            for i in range(len(head)):
                self.permutations(head[0:i] + head[i + 1:], tail + head[i])

    def evaluate(self, combination):
        cost = 0
        for i, c in enumerate(combination):
            if c == 'B':
                color_index = 0
            elif c == 'G':
                color_index = 1
            else:
                color_index = 2
            for b in range(0, 3):
                cost += self.cost_list[b * 3 + color_index]
            cost -= self.cost_list[i * 3 + color_index]
        return cost


    def print_optimal_movement(self, input_file_name,output_file_name):
        with open(input_file_name, "r") as input_file, open(output_file_name,"w") as output_file:
            for line in input_file:
                self.cost_list = map(int, line.split())
                self.permutations('BGC')
                self.permutation_list.sort()
                cost_list = map(lambda p: self.evaluate(p), self.permutation_list)
                val, idx = min((val, idx) for (idx, val) in enumerate(cost_list))
                output_file.write("%s %d\n" % (self.permutation_list[idx], val))
        input_file.close()
        output_file.close()