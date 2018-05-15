def read_inputs(input_file_name):
    with open(input_file_name, "r") as input_file:
        line = input_file.readline()
        while line != "":
            dimension = int(line)
            arbitrage = Solution(dimension)
            for n in range(0, dimension):
                exchange_list = map(float, input_file.readline().split())
                exchange_list.insert(n, 1)
                for i,e in enumerate(exchange_list):
                    arbitrage.exchange_rate_table[n][i][1] = e
            print(arbitrage.exchange_rate_table)
            arbitrage.find_smallest()
            # arbitrage.print_result()
            line = input_file.readline()


class Solution:
    def __init__(self, n):
        self.total = n
        self.exchange_rate_table = []
        for a in range(0,n):
            a_list = []
            for b in range(0,n):
                b_list = []
                for c in range(0,n):
                    b_list.append(0.0)
                a_list.append(b_list)
            self.exchange_rate_table.append(a_list)


    def find_smallest(self):
        for s in range(1, self.total):
            for i in range(0, self.total):
                for j in range(0, self.total):
                    for k in range(0, self.total):
                        self.exchange_rate_table[i][j][s] = max(self.exchange_rate_table[i][j][s], self.exchange_rate_table[i][j][s-1]*self.exchange_rate_table[j][k][1])
        print(self.exchange_rate_table)

read_inputs("input.txt")
