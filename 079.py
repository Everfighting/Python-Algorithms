#!/usr/bin/python
# -*- coding: UTF-8 -*-

if __name__ == '__main__':
	str1 = raw_input('input string:\n')
	str2 = raw_input('input string:\n')
	str3 = raw_input('input string:\n')
	print str1, str2, str3

	if str1 > str2: str1, str2 = str2, str1
	if str1 > str3: str1, str3 = str3, str1
	if str2 > str3: str2, str3 = str3, str2

	print 'after being sorted.'
	print str1, str2, str3

if __name__ == '__main__':
	str4 = raw_input('input string:\n')
	str5 = raw_input('input string:\n')
	str6 = raw_input('input string:\n')
	print str4, str5, str6

	li = [str1, str2, str3]
	li.sort()

	print 'after being sorted.'
	for key in li:
		print key,