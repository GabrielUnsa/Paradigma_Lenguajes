import os
class Archivo(object):

	def __init__(self):
		self.__Archivo=''
		self.__ArchivoEncrip=''
		
	def Nombre(self):
		return self.__ArchivoEncrip.name
	
	def Crear(self):
		nombre=str(raw_input("Nombre de Archivo: "))
		nombre=nombre+'.txt'
		print "Si existe el archivo este se sobreescribira"
		self.__Archivo=open(nombre,"w")
	
	def Crea_Encrip(self):
		self.__ArchivoEncrip=open(self.__Archivo.name[:-4]+'encrip.txt',"w")

	def Abrir(self):
		nombre=str(raw_input("Ingrese el Nombre: "))
		nombre=nombre+'.txt'
		try:
			self.__Archivo=open(nombre)
		except:
			print("El archivo no existe")

	def Agrega(self):
		nombre=str(raw_input("Ingrese el Nombre: "))
		nombre=nombre+'.txt'
		self.__Archivo=open(nombre,"a")
		self.__Archivo.write('\n')
		print("Lineas a agregar: ")
	
	def Escribe(self):
		print "Para guardar ponga en una linea save.-"
		texto='a'
		i=0;
		while(not texto=='save.-'):
			texto=str(raw_input("Linea %d: "%i))
			if(not (texto=='save.-')):
				i=i+1 
				self.__Archivo.write(texto)
				self.__Archivo.write('\n')
		self.__Archivo.close()
	
	def Escribe(self,cadena):
		self.__ArchivoEncrip.write(cadena)
		self.__ArchivoEncrip.write('\n')
		
				
	def Muestra(self):
		linea=self.__Archivo.readline()
		print self.__Archivo.name
		print linea
		while linea!='':
			linea=self.__Archivo.readline()
			print linea

	def Linea(self):
		try:
			linea=self.__Archivo.readline()
			return linea
		except:
			print "No abriste ningun archivo"

	def Cierra(self):
		try:
			self.__Archivo=self.__Archivo.close()
		except:
			print "Se produjo un error al cerrar el archivo"
			
	def CierraEncrip(self):
		try:
			self.__ArchivoEncrip=self.__ArchivoEncrip.close()
		except:
			print "Se produjo un error al cerrar el archivo"
