# coding: utf-8

def twoSum(arr, target):
	"""
	字典其实是散列表的一种, 利用这一特性
	效率会大大提高	
	"""
	dict_temp = {}
	for index, value in enumerate(arr):
		if target - value in dict_temp:
			return [dict_temp[target - value], index]
		dict_temp[value] = index


if __name__ == '__main__':
	arr = [1, 3, 8]
	target = 11
	print(twoSum(arr, target))