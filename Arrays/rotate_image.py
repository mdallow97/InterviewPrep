# 1_11
# Rotate Image

def rotate(matrix):
	return zip(*matrix[::-1])


matrix = [
  	[1,2,3],
 	[4,5,6],
 	[7,8,9]
]

print(rotate(matrix))
