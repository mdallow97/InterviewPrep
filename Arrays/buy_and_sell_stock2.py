# 1_2
# Best time to buy and sell stock 2
# While stock[i+1] - stock[i]


def maxProfit(prices):
	total = 0
	i = 0

	while i < len(prices)-1:
		if prices[i] < prices[i+1]:
			print("buy price at index ", i)
			j = i+1
			while j < len(prices) - 1 and prices[j] < prices[j+1]:
				j+=1
			print("sell price at index ", j)
			total += prices[j] - prices[i]

			i = j
		i += 1

	return total


print(maxProfit([7,1,5,3,6,4]))