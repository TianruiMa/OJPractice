class SkylineAlter:
    def __init__(self, input_file_name):
        self.building_block_list = []
        right_most = 0
        with open(input_file_name, "r") as input_file:
            for line in input_file:
                build_triple = map(int, line.split())
                self.building_block_list.append(build_triple)
                right_most = max(right_most, build_triple[2])
        input_file.close()
        self.left_most = self.building_block_list[0][0]
        print("left most %d right most %d" % (self.left_most, right_most))
        self.height_list = [0] * (right_most - self.left_most + 1)
        # print(len(self.height_list))

    def combine_heights(self, output_filename):
        combined_height_list = []
        height = 0
        for i, h in enumerate(self.height_list):
            if height != h:
                combined_height_list.append(i + self.left_most)
                combined_height_list.append(h)
                height = h
        with open(output_filename, "w") as output_file:
            for c in combined_height_list:
                output_file.write("%d " % c)
        output_file.close()

    def match_height(self, output_filename):
        for building in self.building_block_list:
            on_map_left = building[0] - self.left_most
            on_map_right = building[2] - self.left_most

            for d in range(on_map_left, on_map_right):
                self.height_list[d] = max(building[1], self.height_list[d])
        self.combine_heights(output_filename)


skyline = SkylineAlter("input.txt")
skyline.match_height("output.txt")
