class Solution:
	def longestCommonPrefix(self, strs: List[str]) -> str:
		res = ""
		strs.sort()
		if len(strs) == 1:
			return strs[0]
		first = strs[0]
		second = strs[-1]

		for i in range(len(first)):
			if first[i] == second[i]:
				res += first[i]
			else: break

		return res