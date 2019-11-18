# 1_3
# Group anagrams

from itertools import permutations
import collections

def findAnagram(strs, s):
	perms = list(permutations(s))
	perms.pop(0)

	combos = ["".join(perm) for perm in perms]

	for i in range(len(strs)):
		if strs[i] in combos:
			anagram = strs.pop(i)
			return strs, anagram

	return strs, ""

def groupAnagrams(strs):
	result = []
	while len(strs) > 0:
		s = strs.pop(0)
		anagrams = [s]

		if s in strs:
			anagrams.append(s)
			strs.pop(strs.index(s))

		strs, anagram = findAnagram(strs, s)
		while len(anagram) > 0:
			anagrams.append(anagram)
			strs, anagram = findAnagram(strs, s)
		result.append(anagrams)

	return result


def groupAnagrams1(strs):
	dic = {}
	result = []
	while len(strs) > 0:
		s = strs.pop(0)
		perms = list(permutations(s))

		for perm in perms:
			combo = "".join(perm)
			if combo in dic:
				dic[combo].append(s)
				break
		else:
			dic[s] = [s]

	for key in dic.keys():
		result.append(dic[key])

	return result


def groupAnagrams2(strs):
	dic = collections.defaultdict(list)
	for s in strs:
		dic[tuple(sorted(s))].append(s)

	return dic.values()


print(groupAnagrams2(["eat", "tea", "tan", "ate", "nat", "bat"]))