class Solution:
    """
    @param grid: an integer matrix
    @return: an integer
    """

    def explore(self, grid, r, c):
        rbound = len(grid)
        cbound = len(grid[0])

        if r >= rbound or c >= cbound or r < 0 or c < 0 or grid[r][c] == 0:
            return
        else:
            grid[r][c] = 0
            self.explore(grid, r, c + 1)
            self.explore(grid, r, c - 1)
            self.explore(grid, r + 1, c)
            self.explore(grid, r - 1, c)

    def numIslandCities(self, grid):
        # Write your code here

        row = len(grid)
        col = len(grid[0])
        res = 0
        for r in xrange(row):
            for c in xrange(col):
                curr = grid[r][c]
                if curr == 2:
                    res += 1
                    self.explore(grid, r, c)
        return res