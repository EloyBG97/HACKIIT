#!/usr/bin/python
#-*- encoding: utf-8 -*-

import sys

def ftos(ifile):
	with open(ifile, 'r') as letter:
    		msg = letter.read()

	return msg

def CesarCypher(n,msg):
	msg2 = ''
	n = int(n)

	#Códigos ASCII
	cod_a = ord('a')
	cod_z = ord('z')
	cod_A = ord('A')
	cod_Z = ord('Z')

	#Nº letras mayúsculas/minúsculas en código ASCII
	nletras = cod_z - cod_a + 1

	inc_m = n - cod_a
	inc_M = n - cod_A

	for c in msg:	
		ascii = ord(c)

		if ascii >= cod_a and ascii <= cod_z: 
			msg2 +=  chr((ascii + inc_m) % nletras + cod_a)

		elif ascii >= cod_A and ascii <= cod_Z:
			msg2 += chr((ascii + inc_M) % nletras + cod_A)

		else:
			msg2 += c

	return msg2
	
	
if __name__ == '__main__':
	if len(sys.argv) != 3: 
		print >> sys.stderr, 'Uso ' + sys.argv[0] + ' <n_desplazamientos> <fichero_cifrado>\n'
		sys.exit(2)
 
	n = sys.argv[1]
	letter = sys.argv[2]

	msg = ftos(letter)

	msg2 = CesarCypher(n,msg)
	print '\n' + msg2 + "\n"
