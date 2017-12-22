#!/usr/bin/python
#-*- encoding: utf-8 -*-

import sys
from Tkinter import *

def ftos(ifile):
	with open(ifile, 'r') as letter:
    		msg = letter.read()

	return msg

def CesarCypher():
	ifile = file_input.get()
	n = offset_input.get()
 
	msg = ftos(ifile)
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

	solution.config(text = msg2)
	
	
if __name__ == '__main__':
	raiz = Tk()
	raiz.title('Cesar Cypher')

	ifile = ""
	n = ""
	
	mainframe = Frame(raiz)
	mainframe.grid(column=0,row=0,padx=(50,50),pady=(20,20))


	file_tag = Label(mainframe,text='Introduzca el fichero: ')
	file_tag.grid(column=1,row=1)	

	file_input = Entry(mainframe,width = 10, textvariable= ifile)
	file_input.grid(column = 2, row = 1)

	offset_tag = Label(mainframe,text='Introduzca el desplazamiento: ')
	offset_tag.grid(column=1,row=2)	

	offset_input = Entry(mainframe,width = 10, textvariable= n)
	offset_input.grid(column = 2, row = 2)

	cypher_button = Button(mainframe, text='Descifrar', command = CesarCypher)
	cypher_button.grid(column = 2, row =3)

	solution = Label(mainframe,text='(Nothing)',relief="sunken", borderwidth=2, bg="white")
	solution.grid(column=1,row=5)	

	raiz.mainloop()
