class Solution:
    """
    @param logs: the logs
    @return: the log after sorting
    """

    def logSort(self, logs):
        # Write your code here
        component_one_list = filter(lambda x: not x.split()[1].isdigit(), logs)
        component_two_list = filter(lambda x: x.split()[1].isdigit(), logs)
        component_one_list = sorted(sorted(component_one_list, key=lambda x: x.split()[0]),
                                    key=lambda x: x[x.find(" ") + 1:])
        component_one_list.extend(component_two_list)
        return component_one_list
