import itertools


def rearrange_list(my_list):
    new_list = list(my_list)
    new_list.pop(0)
    new_list.append(new_list[0])
    return new_list


def find_dup(my_list):
    start = my_list[0]
    dup_list = []
    new_combination = rearrange_list(my_list)
    while new_combination[0] != start:
        dup_list.append(new_combination)
        new_combination = rearrange_list(new_combination)
    return dup_list


def read_inputs(input_file_name):
    with open(input_file_name, "r") as input_file:
        line = input_file.readline()
        while line != "":
            dimension = int(line)
            arbitrage = ArbitrageAlter(dimension)
            for n in range(0, dimension):
                exchange_list = map(float, input_file.readline().split())
                exchange_list.insert(n, 1)
                arbitrage.exchange_rate_table.append(exchange_list)
            arbitrage.print_result()
            line = input_file.readline()


class ArbitrageAlter:
    def __init__(self, n):
        self.total = n
        self.exchange_rate_table = []
        self.combination_list = []

    def generate_whole_list(self):
        for start in range(0, self.total):
            not_in = [e for e in range(0, self.total) if e != start]
            if len(not_in) == 1:
                new_list = [start, not_in[0], start]
                self.combination_list.append(new_list)
                continue
            for length in range(1, self.total - 1):
                my_list = list(itertools.permutations(not_in, length))
                for combinations in my_list:
                    new_list = [start]
                    for x in combinations:
                        new_list.append(x)
                    new_list.append(start)
                    self.combination_list.append(new_list)

    def eliminate_duplication(self):
        for stack in self.combination_list:
            dup_list = find_dup(stack)
            for d in dup_list:
                if d in self.combination_list:
                    self.combination_list.remove(d)

    def find_success(self):
        for stack in self.combination_list:
            result = 1
            for index in range(0, self.total - 2):
                buyer = stack[index]
                buyee = stack[index + 1]
                result *= self.exchange_rate_table[buyer][buyee]
            if result > 1.01:
                print(map(lambda x: x + 1, stack))
                return
        print("no arbitrage sequence exists")

    def print_result(self):
        self.generate_whole_list()
        self.combination_list.sort(key=len, reverse=False)
        self.eliminate_duplication()
        self.find_success()


read_inputs("input.txt")
