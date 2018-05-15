
def if_contains(a, b):
    return a[0] <= b[0] and a[2] >= b[2] and a[1] >= b[1]

def if_left_dominates(a, b):
    return b[0] in range(a[0], a[2]) and a[2] < b[2] and a[1] > b[1]

def if_right_dominates(a,b):
    return b[2] in range(a[0], a[2]) and b[0] < a[0] and a[1] > b[1]

def if_outrage(a ,b):
    return a[0] <= b[0] and a[2] >= b[2] and a[1] <= b[1]

class Skyline:
    def __init__(self, input_file_name):
        self.building_block_list = []
        with open(input_file_name, "r") as input_file:
            for line in input_file:
                build_triple = map(int,line.split())
                self.building_block_list.append(build_triple)
        input_file.close()

    def cut_building(self, new_building, edited_buildings):
        tmp = list(edited_buildings)
        for eb in edited_buildings:
            if if_contains(eb, new_building):
                # print("eb :", eb),
                # print(" contains "),
                # print("nb :", new_building)
                if new_building in tmp: tmp.remove(new_building)
                return tmp
            elif if_contains(new_building, eb):
                # print("nb :",new_building),
                # print(" contains "),
                # print("eb :",eb)
                tmp.remove(eb)
                if new_building not in tmp: tmp.append(new_building)
            elif if_left_dominates(eb, new_building):
                # print("eb :",eb),
                # print(" left dominate "),
                # print("nb :",new_building)
                if new_building in tmp: tmp.remove(new_building)
                tmp.append([eb[2],new_building[1],new_building[2]])
            elif if_left_dominates(new_building, eb):
                # print("nb :",new_building),
                # print(" left dominate "),
                # print("eb :",eb)
                if new_building not in tmp:tmp.append(new_building)
                tmp.remove(eb)
                tmp.append([new_building[2],eb[1],eb[2]])
            elif if_right_dominates(eb, new_building):
                # print("eb :",eb),
                # print(" right dominate "),
                # print("nb :",new_building)
                if new_building in tmp:tmp.remove(new_building)
                tmp.append([new_building[0],new_building[1],eb[0]])
            elif if_right_dominates(new_building, eb):
                # print("nb :",new_building),
                # print(" right dominate "),
                # print("eb :",eb)
                if new_building not in tmp:tmp.append(new_building)
                tmp.remove(eb)
                tmp.append([eb[0],eb[1],new_building[0]])
            elif if_outrage(eb, new_building):
                # print("eb :",eb),
                # print(" outrage "),
                # print("nb :",new_building)
                if new_building not in tmp:tmp.append(new_building)
                tmp.remove(eb)
                tmp.append([eb[0],eb[1],new_building[0]])
                tmp.append([new_building[2],eb[1],eb[2]])
            elif if_outrage(new_building, eb):
                # print("nb :",new_building),
                # print(" outrage "),
                # print("eb :",eb)
                if new_building in tmp:tmp.remove(new_building)
                tmp.append([new_building[0],new_building[1],eb[0]])
                tmp.append([eb[2],new_building[1],new_building[2]])
            else:
                # print("eb :",eb),
                # print("not related"),
                # print("nb :",new_building)
                if new_building not in tmp:tmp.append(new_building)
            # print(tmp)
        return tmp


    def combine_building(self,edited_buildings):
        combined = []
        length = len(edited_buildings)
        for index in range(0, length-1):
            first = edited_buildings[index]
            second = edited_buildings[index + 1]
            combined.extend(first[0:2])
            if first[2] != second[0]:
                combined.extend([first[2],0])

        combined.extend(edited_buildings[-1])
        combined.append(0)
        return combined


    def redraw_buildings(self,output_file_name):
        result = []
        edited_buildings = []
        for building in self.building_block_list:
            if len(edited_buildings) == 0:
                edited_buildings.append(building)
                continue
            edited_buildings = self.cut_building(building, edited_buildings)
        edited_buildings.sort()
        # print(edited_buildings)
        combined_building = self.combine_building(edited_buildings)
        with open(output_file_name,'w') as output_file:
            for cb in combined_building:
                output_file.write("%d " % cb)
        output_file.close()



skyline = Skyline("input.txt")
skyline.redraw_buildings("output.txt")
