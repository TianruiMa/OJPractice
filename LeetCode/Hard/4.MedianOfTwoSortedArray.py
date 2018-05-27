class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        list1, list2, len1, len2 = nums1, nums2, len(nums1), len(nums2)
        if len1 > len2: list1, list2, len1, len2 = list2, list1, len2, len1

        is_odd_length = (len1 + len2) % 2 != 0

        imin, imax, median_position = 0, len1, (len1 + len2 + 1) / 2

        pivot1 = len1 / 2
        pivot2 = median_position - pivot1

        # while imin <= imax:
        while True:
            if pivot1 > 0 and pivot2 < len2 and list1[pivot1 - 1] > list2[pivot2]:
                pivot1 -= 1
                pivot2 += 1
            elif pivot1 < len1 and pivot2 > 0 and list1[pivot1] < list2[pivot2 - 1]:
                pivot1 += 1
                pivot2 -= 1
            else:
                if pivot1 == 0:
                    max_of_left = list2[pivot2 - 1]
                elif pivot2 == 0:
                    max_of_left = list1[pivot1 - 1]
                else:
                    max_of_left = max(list1[pivot1 - 1], list2[pivot2 - 1])

                if is_odd_length: return max_of_left

                if pivot1 == len1:
                    min_of_right = list2[pivot2]
                elif pivot2 == len2:
                    min_of_right = list1[pivot1]
                else:
                    min_of_right = min(list1[pivot1], list2[pivot2])
                return (max_of_left + min_of_right) / 2.0