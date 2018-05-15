def read_inputs(input_file_name):
    with open(input_file_name, "r") as input_file:
        line = input_file.readline()
        while line != "":
            dimension = int(line)
            arbitrage = Arbitrage(dimension)
            for n in range(0, dimension):
                exchange_list = map(float, input_file.readline().split())
                exchange_list.insert(n, 1)
                arbitrage.exchange_rate_table.append(exchange_list)
            arbitrage.print_result()
            line = input_file.readline()


class Arbitrage:
    def __init__(self, n):
        self.total = n
        self.exchange_rate_table = []
        self.success_list = []

    def print_result(self):
        for buyer in range(0, self.total):
            self.check_win(buyer, buyer, 1, [buyer])
        if len(self.success_list) == 0:
            print("no arbitrage sequence exists")
        for x in self.success_list:
            print("%d " % (x+1)),
        print("")

    def forward_checking(self, buyer, starter, result, stack):
        result *= self.exchange_rate_table[buyer][starter]
        if result > 1.01:
            tmp = list(stack)
            tmp.append(starter)
            self.success_list = tmp

    def check_win(self, buyer, starter, result, check_stack):

        for buyee in range(0, self.total):
            tmp_stack = list(check_stack)
            if buyee == buyer or (buyee in tmp_stack): continue
            if len(self.success_list) == 0 : min_length = self.total -1
            else: min_length = len(self.success_list) - 1
            if len(check_stack) >= min_length: break

            tmp_stack.append(buyee)
            rate = self.exchange_rate_table[buyer][buyee]
            self.forward_checking(buyee, starter, result * rate, tmp_stack)
            self.check_win(buyee, starter, result * rate, tmp_stack)

read_inputs("input.txt")