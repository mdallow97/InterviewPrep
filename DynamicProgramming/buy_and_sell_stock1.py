# 6_2
# buying and selling stock

def maxProfit(prices):
	mx = 0
	i = 0
	while i < len(prices)-1:
		j = i+1
		while j < len(prices):
			pos_profit = prices[j] - prices[i]
			if pos_profit > mx:
				mx = pos_profit
			j += 1

		i += 1

	return mx


def maxProfit2(prices):
	min_price = 9999999
	mx = 0
	i = 0

	while i < len(prices):
		if prices[i] < min_price:
			min_price = prices[i]
		elif prices[i] - min_price > mx:
			mx = prices[i] - min_price

		i+=1

	return mx




print(maxProfit([7,6,4,3,1]))
