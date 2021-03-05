# unique_emails.py
from collections import defaultdict

class Solution(object):
	def numUniqueEmails(self, emails):
		"""
		:type emails: List[str]
		:rtype: int
		"""
		name_domains = defaultdict(list)
		numUnique = 0

		for email in emails:
			name,domain = email.split('@')

			try:
				ignore_past = name.find('+')
			except:
				ignore_past = -1

			if ignore_past > 0:
				name = name[:ignore_past]

			name = name.replace('.','')

			if name not in name_domains[domain]:
				name_domains[domain].append(name)
				numUnique += 1

		return numUnique


def main():
	emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]

	sol = Solution()
	print(sol.numUniqueEmails(emails))


if __name__ == '__main__':
	main()