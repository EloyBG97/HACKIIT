#!/usr/bin/python
import sys
import binascii
import string

def loadlist(ifile):
	lst = []

	for line in open(ifile,'r'):
		lst.extend(line.split())

	return lst


if __name__ == '__main__':

	if len(sys.argv) != 2: 
		sys.exit(2)

	char = loadlist(sys.argv[1])

	hexa = set('abcdef')
	msg = ''

	for c in char:
		#OCTAL
		if c[0] == '0':
			msg+=chr(string.atoi(c, 8))

		#HEXADECIMAL
		elif any((d in hexa) for d in c):
			msg+=c.decode('hex')
		
		else:
			#BINARIO
			try:
				msg+=binascii.unhexlify('%x' % int(c,2))
				
			#DECIMAL
			except (ValueError, TypeError) as e:
				msg+=chr(int(c))

	print msg
