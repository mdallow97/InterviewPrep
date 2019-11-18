# 3_7
# number of islands

def deleteIsland(grid, i, j):
	grid[i][j] = "0"
	if i - 1 >= 0 and grid[i-1][j] == "1":
		deleteIsland(grid, i-1, j)

	if i + 1 < len(grid) and grid[i+1][j] == "1":
		deleteIsland(grid, i+1, j)

	if j - 1 >= 0 and grid[i][j-1] == "1":
		deleteIsland(grid, i, j-1)

	if j + 1 < len(grid[0]) and grid[i][j+1] == "1":
		deleteIsland(grid, i, j+1)

def numIslands(grid):
	if len(grid) == 0:
		return 0

	count = 0
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if grid[i][j] == "1":
				count += 1
				deleteIsland(grid, i, j)

	return count


grid_new = [[1,1,0,0,0],
			[1,1,0,0,0],
			[0,0,1,0,0],
			[0,0,0,1,1]]

print(numIslands(grid_new))