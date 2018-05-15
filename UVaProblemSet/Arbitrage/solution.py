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
                    arbitrage.exchange_rate_table[n][i][1] = [e,0]
            # print(arbitrage.exchange_rate_table)
            arbitrage.find_smallest()
            arbitrage.print_result()
            line = input_file.readline()


class Solution:
    def __init__(self, n):
        self.total = n
        self.exchange_rate_table = []
        self.trace_list = []
        for a in range(0,n):
            a_list = []
            for b in range(0,n):
                b_list = []
                for c in range(0,n):
                    b_list.append([0.0,0])
                a_list.append(b_list)
            self.exchange_rate_table.append(a_list)

    def print_result(self):
        for t in self.trace_list:
            print("%d " % t),
        print("\n")

    def trace_back(self, start, end, round):
        if round < 2: return
        last = self.exchange_rate_table[start][end][round][1]
        self.trace_list.insert(0,last+1)
        self.trace_back(start, last, round-1)


    def find_smallest(self):
        for s in range(2, self.total):
            for i in range(0, self.total):
                for j in range(0, self.total):
                    for k in range(0, self.total):
                        # if k == j: continue
                        # if s == 3:
                        #     print(" ---   round %d    ---  " % s)
                        #     print("i=%d,  j=%d,  k=%d" % (i, j, k))
                        #     print("current rate: %f" % self.exchange_rate_table[i][j][s])
                        #     print("middle step from k=%d to j=%d: %f * %f" % (k,j,self.exchange_rate_table[k][j][1], self.exchange_rate_table[i][k][s-1]))
                        # self.exchange_rate_table[i][j][s] = max(self.exchange_rate_table[i][j][s], self.exchange_rate_table[i][k][s-1]*self.exchange_rate_table[k][j][1])
                        if self.exchange_rate_table[i][k][s-1][0]*self.exchange_rate_table[k][j][1][0] > self.exchange_rate_table[i][j][s][0]:
                            self.exchange_rate_table[i][j][s][0] = self.exchange_rate_table[i][k][s-1][0]*self.exchange_rate_table[k][j][1][0]
                            self.exchange_rate_table[i][j][s][1] = k


                        # print("new rate: %f" % self.exchange_rate_table[i][j][s][0])
                        if i == j and self.exchange_rate_table[i][j][s][0] > 1.01:
                            self.trace_list.insert(0,j+1)
                            self.trace_back(i,j,s)
                            self.trace_list.insert(0,j+1)

                            # self.trace_list.pop(0)
                            # self.trace_list.insert(0,j+1)
                            # self.trace_list.append(j+1)
                            # print(self.trace_list)
                            return
        # print(self.exchange_rate_table)
        print("no arbitrage sequence exists")



read_inputs("input.txt")
