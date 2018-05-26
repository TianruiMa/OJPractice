from collections import defaultdict


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        count_dict = defaultdict(int)

        for n in nums:
            count_dict[n] += 1
        bucket = [[] for i in range(max(count_dict.values()))]
        for key, value in count_dict.items():
            bucket[value - 1].append(key)
        res = []
        for i, j in enumerate(bucket[::-1]):
            if k - len(res) == 0: break
            res.extend(j[:min(k - len(res), len(j))])
        return res
