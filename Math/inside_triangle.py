import numpy as np

def inside_triangle(triangle, point):
	def triangle_area(sub_triangle):
		v1 = sub_triangle[1] - sub_triangle[0]
		v2 = sub_triangle[2] - sub_triangle[0]
		return abs(np.linalg.det([v1]+[v2])) / 2

	total_area = triangle_area(triangle)
	print([point, triangle[0], triangle[1]])
	sub1 = triangle_area([point, triangle[0], triangle[1]])
	sub2 = triangle_area([point, triangle[1], triangle[2]])
	sub3 = triangle_area([point, triangle[0], triangle[2]])

	if total_area == sub1 + sub2 + sub3:
		return True
	else:
		return False


def main():
	triangle = np.array([[0,1], [4,1], [2,2]])
	point = np.array([3,1.5])

	print(inside_triangle(triangle, point))

if __name__ == '__main__':
	main()