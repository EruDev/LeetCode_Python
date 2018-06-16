# coding: utf-8

def reverse(x):
	x = str(x)
	if len(x) > 32:
		return 0
	return x[::-1]


x = 123
print(reverse(x)) 