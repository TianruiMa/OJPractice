# from itertools import permutations
# import sys

def timeDifference(next_time, prev_time):
    if next_time == prev_time: return 24 * 60
    next_time = int(next_time) / 100 * 60 + int(next_time) % 100
    prev_time = int(prev_time) / 100 * 60 + int(prev_time) % 100
    return (next_time - prev_time) % (24 * 60)


# def check_valid(time):
#     if int(time[:2]) > 23 or int(time[2:]) > 59:
#         return False
#     return True

class Solution(object):

    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        time = ''.join(time.split(':'))
        my_set = set(time)
        pmts = []
        for a in my_set:
            for b in my_set:
                for c in my_set:
                    for d in my_set:
                        if int(a + b) <= 23 and int(c + d) <= 59:
                            pmts.append(a + b + c + d)
        # pmts = map(lambda x: ''.join(x), list(set(list(permutations(time, 4)))))
        # pmts = filter(lambda x:check_valid(x),pmts)
        # print(pmts)
        pmts = list(set(list(pmts)))

        diff_list = map(lambda x: timeDifference(x, time), pmts)
        res = pmts[diff_list.index(min(diff_list))]
        return res[:2] + ":" + res[2:]

    # def nextClosestTime(self, time):
    #     """
    #     :type time: str
    #     :rtype: str
    #     """
    #     s = set(time)
    #     hour = int(time[0:2])
    #     minute = int(time[3:5])
    #     while True:
    #         minute += 1
    #         if minute == 60:
    #             minute = 0
    #             hour = 0 if hour == 23 else hour + 1
    #         time = "%02d:%02d" % (hour, minute)
    #         if set(time) <= s:
    #             return time
