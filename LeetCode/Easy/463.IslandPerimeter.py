class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        columns = len(grid[0])
        res = 0
        for r in range(rows):
            for l in range(columns):
                if grid[r][l] == 1:
                    res += 4
                    if (r > 0 and grid[r - 1][l]):
                        res -= 2
                    if l > 0 and grid[r][l - 1]:
                        res -= 2
        return res
