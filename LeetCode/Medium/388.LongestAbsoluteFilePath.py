class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        # input_list = input.split("\n")
        # max_char_count = 0
        # length_stack = []
        # for i in input_list:
        #     curr_level = i.count("\t")
        #     i = i.replace("\t","")
        #     length_stack = length_stack[:curr_level]
        #     if '.' not in i: i += '/'
        #     new_char_count = length_stack[-1] + len(i)if len(length_stack)!=0 else len(i)
        #     if '.' not in i:  length_stack.append(new_char_count)
        #     else: max_char_count = max(max_char_count,new_char_count)
        # return max_char_count

        maxlen = 0
        pathlen = {0: 0}
        for line in input.splitlines():
            name = line.lstrip('\t')
            depth = len(line) - len(name)
            if '.' in name:
                maxlen = max(maxlen, pathlen[depth] + len(name))
            else:
                pathlen[depth + 1] = pathlen[depth] + len(name) + 1
        return maxlen