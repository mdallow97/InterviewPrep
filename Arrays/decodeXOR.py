# decodeXOR.py

def decode(encoded, first):
	arr = [first]
	for i in range(len(encoded)):
		arr.append(encoded[i] ^ arr[i])

	return arr

def main():
	print(decode([1,2,3], 1))
	print(decode([6,2,7,3], 4))

if __name__ == '__main__':
	main()
