# k_freq_elements.py
from collections import defaultdict

def kFreqElements(nums, k):
	freq_dictionary = defaultdict(int)

	for num in nums:
		freq_dictionary[num] += 1

	print(freq_dictionary)

	most_frequent = []

	mx = 0
	while k > 0:
		for key in freq_dictionary.keys():
			if freq_dictionary[key] > freq_dictionary[mx]:
				mx = key

		if mx in freq_dictionary:
			most_frequent.append(mx)
			freq_dictionary.pop(mx)
		mx = 0
		k -= 1



	return most_frequent

# return k most frequent elements
def kFreqElements2(nums, k):
	freq_dic = {}

	for num in nums:
		if num in freq_dic:
			freq_dic[num][0] += 1
		else:
			freq_dic[num] = [0,num]

	l = sorted(freq_dic.values())
	l.reverse()
	print(l)
	result = [l[i][1] for i in range(k)]
	return result


print(kFreqElements2([1,1,1,2,2,3], 2))
