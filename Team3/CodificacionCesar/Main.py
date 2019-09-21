import os
from ClsFile import *
from ClsCesar2 import *
def menu():
	os.system("cls")
	op=10
	while(op>8):
		print "1. Crea Archivo"
		print "2. Abrir Archivo"
		print "3. Agrega Texto"
		print "4. Muestra Archivo"
		print "5. Cifrar"
		print "6. Desifrar (clave)"
		print "7. Desifrar (sin clave)"
		print "8. Cerrar Archivo"
		print "0. Salir"
		op=int(raw_input("Opcion: "))
		os.system("cls")
	return op

def main():
	obj1=Cesar()
	op=menu()
	while(not(op==0)):
		if(op==1):
			obj1.Crear()
			obj1.Escribe()
			x=(raw_input("Presione enter para continuar........"))
		elif(op==2):
			obj1.Abrir()
			x=(raw_input("Precione enter para continuar......"))
		elif(op==3):
			obj1.Agrega()
			obj1.Escribe()
			x=(raw_input("Presione enter para continuar........"))
		elif(op==4):
			obj1.Muestra()
			x=(raw_input("Presione enter para continuar........"))
		elif(op==5):
			linea='a'
			obj1.Abrir()
			obj1.Clave()
			obj1.Crea_Encrip()
			while linea!='':
				linea=obj1.Linea()
				obj1.Escribe(obj1.Cifrar(linea))
			print("Se guardo el encriptado en: ")+ obj1.Nombre()
			obj1.CierraEncrip()
			x=(raw_input("Presione enter para continuar........"))
		elif(op==6):
			linea='a'
			obj1.Abrir()
			obj1.Clave()
			obj1.Crea_Encrip()
			while linea!='':
				linea=obj1.Linea()
				obj1.Escribe(obj1.Descifrar(linea))
			print("Se guardo el encriptado en: ")+ obj1.Nombre()
			obj1.CierraEncrip()
			x=(raw_input("Presione enter para continuar........"))
		elif(op==7):
			obj1.Abrir()
			linea='a'
			while linea!='':
				linea=obj1.Linea()
				obj1.Descifrar_Clave(linea)
			x=(raw_input("Presione enter para continuar........"))
		elif(op==8):
			obj1.Cierra()
			x=(raw_input("Presione enter para continuar........"))
		op=menu()

main()
