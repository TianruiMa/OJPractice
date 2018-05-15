class Box:
    def __init__(self, id):
        self.box_id = id
        self.sorted_dimensions = []
        self.contained_in = None


def is_bigger(box_a, box_b):
    for a, b in zip(box_a.sorted_dimensions, box_b.sorted_dimensions):
        if a <= b: return False
    return True


def generate_box(id, line):
    dimension = map(int, line.split())
    dimension.sort()
    new_box = Box(id)
    new_box.sorted_dimensions = dimension
    return new_box


def read_input(input_file_name,output_file_name):
    output_file = open(output_file_name,"w")
    with open(input_file_name, "r") as input_file:
        number_of_boxes = 0
        box_id = 100
        stack_boxes = None
        for line in input_file:
            # print("number_of_boxes: %d, box_id: %d" %(number_of_boxes,box_id))
            if box_id > number_of_boxes:
                (number, dimension) = map(int, line.split())
                stack_boxes = StackingBoxes(number, dimension,output_file)
                # print("stack_boxes info: Dlength %d" % len(stack_boxes.d))
                number_of_boxes = number
                box_id = 1
            else:
                stack_boxes.box_list.append(generate_box(box_id, line))
                if box_id == number_of_boxes: stack_boxes.print_longest()
                box_id += 1


class StackingBoxes:
    def __init__(self, number, d, outputfile):
        self.length = number
        self.box_list = []
        self.compare_matrix = []
        self.dimension = d
        self.link = [0] * self.length
        self.pre = [-1] * self.length
        self.output_file = outputfile

    def dp_solver(self, index):
        if self.link[index] > 0: return self.link[index]
        self.link[index] = 1
        for j in range(0, self.length):
            if is_bigger(self.box_list[j], self.box_list[index]) and self.dp_solver(j) + 1 > self.link[index]:
                self.link[index] = self.link[j] + 1
                self.pre[index] = j
        return self.link[index]

    def print_longest(self):
        max_link_box = 0
        for i in range(0, self.length):
            if self.dp_solver(i) > self.dp_solver(max_link_box):
                max_link_box = i
        self.output_file.write("%d\n" % self.link[max_link_box])
        self.print_int(max_link_box)

    def print_int(self, integer):
        if self.pre[integer] != -1:
            self.output_file.write("%d " % (integer + 1))
            self.print_int(self.pre[integer])
        else:
            self.output_file.write("%d\n" % (integer + 1))


