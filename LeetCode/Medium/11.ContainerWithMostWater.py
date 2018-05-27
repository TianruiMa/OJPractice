class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        start = 0
        end = len(height) - 1
        max_area = 0
        while start < end:
            width = end - start
            if height[start] < height[end]:
                min_height = height[start]
                start += 1
            else:
                min_height = height[end]
                end -= 1

            area = min_height * width
            if max_area < area: max_area = area
        return max_area

