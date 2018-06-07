# coding: utf-8

def lengthOfLongestSubstring(s):
		max_len = 0
		if len(s) == 1 or len(s) == 0:
			max_len = len(s)
		else:
			for i in range(0, len(s) - 1):
				for j in range(1, len(s)):
					# 判断s[j]是否在切片中, 在的话说明s[i,j-1]是一个子串, 把它与历史最大值比较, 不再该切片中, 说明子串还可以更长(因为s[j]本身没出现过)
					if s[j] in s[i:j]:
						right = j
						left = i
						max_len = j - i
					elif j == len(s) - 1: # 要考虑到 j 自加1, 但s[j]一直如果不再该切片中, 得注意有个最大值, 也就是len(s)-1
						if max_len < j -i + 1: # 当j加到最尾部字符还没出现过, 说明从i到最后一个字符就是该子串了, 不用再往后让j 再加了(类似于溢出情况)
							max_len = j - i + 1
			return max_len