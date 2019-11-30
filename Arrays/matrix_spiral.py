# matrix_spiral.py

def matrixSpiral(matrix):
	result = []
	while matrix:
		# go right
		for item in matrix.pop(0):
			result.append(item)
		if not matrix or not matrix[0]:
			break

		# go down
		i = len(matrix[0])-1
		for j in range(len(matrix)):
			result.append(matrix[j].pop(i))
		if not matrix:
			break

		# go left
		for item in reversed(matrix.pop(len(matrix)-1)):
			result.append(item)
		if not matrix or not matrix[0]:
			break

		# go up
		current_index = len(result)
		for j in range(len(matrix)):
			result.insert(current_index, matrix[j].pop(0))

	return result


print(matrixSpiral([[1,11],[2,12],[3,13],[4,14],[5,15],[6,16],[7,17],[8,18],[9,19],[10,20]]))
