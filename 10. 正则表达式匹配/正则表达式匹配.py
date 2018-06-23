# coding: utf-8
import re

def re_match(s, p):
	result = ''
	if s and [item for item in s if ord(item) in list(range(97, 123))]:
		result = p.findall(s)
		print(result)
	return result


if __name__ == '__main__':
	s = 'dsahlkfas'
	p = re.compile(r'[a-z\.\*]+')
	print(re_match(s))