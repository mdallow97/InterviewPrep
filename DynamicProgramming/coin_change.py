# coin_change.py
from collections import defaultdict

def coinChange(coins, amount):
	matrix = [[0 for i in range(amount+1)] for i in range(len(coins)+1)]
	for i in range(1, amount+1):
		matrix[0][i] = float('inf')

	for i in range(1,len(coins)+1):
		for j in range(1, amount+1):

			if coins[i-1] == j:
				matrix[i][j] = 1
			elif coins[i-1] > j:
				matrix[i][j] = matrix[i-1][j]
			else:
				matrix[i][j] = min(matrix[i-1][j], 1+matrix[i][j-coins[i-1]])

	if matrix[-1][-1] == float('inf'):
		return -1
	else:
		return matrix[-1][-1]



print(coinChange([3,5,10,25], 2))
# print(coinChange([186,419,83,408], 6249))
