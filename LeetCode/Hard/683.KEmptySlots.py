import sys


class Solution(object):
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """

        class Bucket:
            def __init__(self):
                self.leftmost_pot = sys.maxint
                self.rightmost_pot = -1

            def insert(self, pot):
                self.leftmost_pot = min(self.leftmost_pot, pot)
                self.rightmost_pot = max(self.rightmost_pot, pot)

        n_buckets = len(flowers) / (k + 1) + 1
        bucket_list = []
        for i in range(n_buckets):
            bucket_list.append(Bucket())

        for pot in flowers:
            bucket_pos = (pot - 1) / (k + 1)
            bucket_list[bucket_pos].insert(pot)
            if pot == bucket_list[bucket_pos].leftmost_pot and bucket_pos > 0:
                if bucket_list[bucket_pos - 1].rightmost_pot == pot - k - 1:
                    return flowers.index(pot) + 1
            if pot == bucket_list[bucket_pos].rightmost_pot and bucket_pos < n_buckets - 1:
                if bucket_list[bucket_pos + 1].leftmost_pot == pot + k + 1:
                    return flowers.index(pot) + 1
        return -1


print(Solution().kEmptySlots([6,5,8,9,7,1,10,2,3,4],2))





