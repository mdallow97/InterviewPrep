#surface_area_3d.py

def surfaceArea(grid):
	"""
	:type grid: List[List[int]]
	:rtype: int
	"""
	zeros = [0 for i in range(len(grid[0])+2)]
	grid = [zeros] + [[0] + sublist + [0] for sublist in grid] + [zeros]

	surface_area = 0
	for i in range(1, len(grid) - 1):
		for j in range(1, len(grid[0]) - 1):
			if grid[i][j] == 0:
				continue
			
			tower_area = (grid[i][j] * 4) + 2
			print(tower_area)
			# check above
			tower_area -= min([grid[i][j], grid[i-1][j]])
			# check below
			tower_area -= min([grid[i][j], grid[i+1][j]])
			# check left
			tower_area -= min([grid[i][j], grid[i][j-1]])
			# check right
			tower_area -= min([grid[i][j], grid[i][j+1]])

			surface_area += tower_area

	return surface_area

def main():
	print(surfaceArea([[1,0],[0,2]]))

if __name__ == "__main__":
	main()