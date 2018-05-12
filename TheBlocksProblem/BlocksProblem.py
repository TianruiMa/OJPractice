class Block():
    def __init__(self):
        self.blockId = -1
        # self.lastPosition = -1;
        self.last_block = None
        self.next_block = None
        self.slot_number = -1


class BlocksProblem:

    def __init__(self, filename):
        input_file = open(filename, "r")
        num_of_blocks = int(input_file.readline())
        input_file.close()
        self.block_table = []
        self.block_list = []
        for index in range(0, num_of_blocks):
            default_block = Block()
            default_block.slot_number = index
            init_block = Block()
            init_block.blockId = index
            self.append_to(init_block, default_block)
            self.block_table.append(default_block)
            self.block_list.append(init_block)

    def change_slot_number(self, block, slot_number):
        if block is None: return
        block.slot_number = slot_number
        self.change_slot_number(block.next_block, slot_number)

    def append_to(self, block_a, block_b):
        if block_a.last_block is not None: block_a.last_block.next_block = None
        block_a.last_block = block_b
        block_b.next_block = block_a
        self.change_slot_number(block_a, block_b.slot_number)

    def find_top_block(self, block):
        if block.next_block is None: return block
        return self.find_top_block(block.next_block)

    def return_to_initial_position(self, block):
        if block is None: return
        top_block = self.find_top_block(self.block_table[block.blockId])
        self.append_to(block, top_block)
        self.return_to_initial_position(block.next_block)

    def move_onto(self, block_a, block_b):
        self.return_to_initial_position(block_a.next_block)
        self.pile_onto(block_a, block_b)

    def move_over(self, block_a, block_b):
        self.return_to_initial_position(block_a.next_block)
        self.pile_over(block_a, block_b)

    def pile_onto(self, block_a, block_b):
        self.return_to_initial_position(block_b.next_block)
        self.append_to(block_a, block_b)

    def pile_over(self, block_a, block_b):
        top_block = self.find_top_block(self.block_table[block_b.slot_number])
        self.append_to(block_a, top_block)

    def illegal(self, block_a, block_b):
        return block_a.slot_number == block_b.slot_number

    def write_to_file(self, output_file_name):
        output_file = open(output_file_name,"w")
        for default_block in self.block_table:
            block_string = self.generate_block_string(default_block.next_block)
            next_block = default_block.next_block
            # print("%d: %s " % (default_block.slot_number, block_string))
            output_file.write("%d:%s\n" % (default_block.slot_number, block_string))
        output_file.close()

    def generate_block_string(self,block):
        if block is None: return ""
        return " " +str(block.blockId) + self.generate_block_string(block.next_block)

    def actions(self, input_file_name, output_file_name):
        input_file = open(input_file_name, "r")
        num_of_blocks = int(input_file.readline())
        for lines in input_file:
            instruction = lines.split()
            action = instruction[0]
            if action == 'quit': break
            adv = instruction[2]
            block_a = self.block_list[int(instruction[1])]
            block_b = self.block_list[int(instruction[3])]
            if self.illegal(block_a, block_b): continue
            if adv == 'onto':
                if action == 'move': self.move_onto(block_a, block_b)
                else: self.pile_onto(block_a, block_b)
            elif action == 'move': self.move_over(block_a, block_b)
            else: self.pile_over(block_a, block_b)
        self.write_to_file(output_file_name)




# block_problem = BlocksProblem("TestCases.txt")
# block_problem.actions("TestCases.txt")