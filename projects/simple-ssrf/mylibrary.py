# simple 'library' to fuzz for SSRF vulnerability
import os
import requests
import http
import urllib3
import sys

def function_to_test(data):

	nothing = []

	if data[4:6] == 'EF':
		if data[0:2] == 'AB':
			if data[2:4] == 'CD':
				exec(f'curl {data[6:]}')
			else:
				nothing.append('a')
		else:
			nothing.append('b')
	else:
		nothing.append('c')

	nothing.append('d')
	for n in nothing:
		print(f'here is some of my nothing: {n}')

	return 0