# set_matrix_zeroes.py

def setZeroes(matrix):
	"""
	:type matrix: List[List[int]]
	:rtype: None Do not return anything, modify matrix in-place instead.
	"""

	cols = []
	rows = []

	row_zero = [0 for i in range(len(matrix[0]))]

	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			if matrix[i][j] == 0:
				print(i,j)
				rows.append(i)
				cols.append(j)

	for i in range(len(matrix)):
		if i in rows:
			matrix[i] = row_zero
			continue

		for j in range(len(matrix[0])):
			if j in cols:
				matrix[i][j] = 0


def main():
	setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]])

if __name__ == "__main__":
	main()