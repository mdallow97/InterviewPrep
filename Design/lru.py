# lru.py

class LRUcache:
	def __init__(self, size):
		self.size = size
		self.cache = {}
		self.lru = [] # beginning of the array is the LRU

	def put(self, key, value):
		
		if key in self.cache:
			# update it as recently used
			index = self.lru.index(key)
			self.lru.pop(index)
		elif len(self.lru) >= self.size:
			# check if there is space in cache
			index = self.lru.pop(0)
			self.cache.pop(index)
			print("Evicting key ", index)

		self.lru.append(key)
		self.cache[key] = value


	def get(self, key):
		if key in self.cache:
			# Update LRU
			index = self.lru.index(key)
			self.lru.pop(index)
			self.lru.append(key)

			print(self.cache[key])
			return self.cache[key]

		else:
			print("-1")
			return -1


cache = LRUcache(2)

cache.put(1,1)
cache.put(2,2)
cache.get(1)
cache.put(3,3)
cache.get(2)
cache.put(4,4)
cache.get(1)
cache.get(3)
cache.get(4)