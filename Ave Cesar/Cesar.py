#!/usr/bin/python
#-*- encoding: utf-8 -*-

import sys

def ftos(ifile)
	msg = ''
	 
	with open(ifile, 'r') as letter:
    		msg += letter.read()

	return msg

def CesarCypher(n,msg):
	msg2 = ''

	#Codigos ASCII
	cod_a = ord('a')
	cod_z = ord('z')
	cod_A = ord('A')
	cod_Z = ord('Z')

	#Nº letras mayusculas/minusculas en código ASCII
	nletras = cod_z - cod_a + 1

	inc_m = int(n) - cod_a
	inc_M = int(n) - cod_A

	for c in msg:
		if ord(c) >= cod_a and ord(c) <= cod_z:
			msg2 += chr((ord(c) + inc_m) % nletras + cod_a)

		elif ord(c) >= cod_A and ord(c) <= cod_Z:
			msg2 += chr((ord(c) + inc_M) % nletras + cod_A)

		else:
			msg2 += c

	return msg2
	
	
if __name__ == '__main__':
	if len(sys.argv) != 3: 
		print 'Uso ' + sys.argv[0] + ' <n_desplazamientos> <fichero_cifrado>\n'
		sys.exit(2)
 
	n = sys.argv[1]
	letter = sys.argv[2]

	msg = ftos(letter)

	msg2 = CesarCypher(n,msg)
	print msg2 + "\n"
