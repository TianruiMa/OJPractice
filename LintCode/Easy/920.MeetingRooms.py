"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """

    def canAttendMeetings(self, intervals):
        # Write your code here
        # if len(intervals) == 0:
        #     return True
        # day_start = min(x.start for x in intervals)
        # day_end = max(x.end for x in intervals)

        # day_scheduele = [0] * (day_end - day_start)

        # for m in intervals:
        #     for x in range(m.start,m.end):
        #         if day_scheduele[x-day_start] == 1:
        #             return False
        #         day_scheduele[x-day_start] = 1
        # return True

        # schedule = []

        # for interval in intervals:
        #     for s in schedule:
        #         if not (interval.end <= s.start or interval.start >= s.end):
        #             return False
        #     schedule.append(interval)
        # return True

        intervals = sorted(intervals, key=lambda x: x.start)
        last = None
        for interval in intervals:
            if last is None:
                last = interval
                continue
            if interval.start < last.end:
                print("interval", interval.start, interval.end)
                print("last", last.start, last.end)
                return False
            last = interval
        return True
