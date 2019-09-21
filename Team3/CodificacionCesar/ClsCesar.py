import os
from ClsFile import * 
class Cesar(Archivo):
	
	def __init__(self):
		super(Cesar,self).__init__()
		self.__abc='abcdefghijklmnopqrstuvwxyz., '
		self.__Clave=0

	def Setabc(self,abc):
		self.__abc=abc

	def Getabc(self):
		return self.__abc

	def SetClave(self,clave):
		self.__Clave=clave

	def GetClave(self):
		return self.__Clave

	def Clave(self):
		clave=int(raw_input("Clave: "))
		while(clave>26):
			clave=int(raw_input("Clave: "))
		self.__Clave=clave
		
	def Cifrar(self,linea):
		"""
		description: codifica el texto que recibe como parametro, utilizando clave
        parametro texto: texto a codificar
        return: devuelve el texto codificado
		"""
		texto_cifrado=''
		for letra in linea:
			suma=self.__abc.find(letra) + self.__Clave #la posición donde inicia la letra y suma la clave
			modulo=int(suma)%len(self.__abc)
			texto_cifrado=texto_cifrado+str(self.__abc[modulo]) #str tranforma el dato en cadena en la posicion del modulo 
			                                                    #y va formando el texto cifrado
		return texto_cifrado

	def Descifrar(self,linea):
		"""
		description: decodifica el texto que recibe como parametro con la clave que utilizo para codificar
        parametro: texto a decodificar
        return: devuelve el texto decodificado
		"""
		texto_descifrado=''
		linea=linea.replace('\n','')
		for letra in linea:
			suma=self.__abc.find(letra) - self.__Clave #Le resto la clave que utilizo para codificar y volver al mensaje
			modulo=int(suma)%len(self.__abc)
			texto_descifrado=texto_descifrado+str(self.__abc[modulo])  #str tranforma el dato en cadena en la posicion del modulo 
			                                                           #y va descifrando el texto
		return texto_descifrado	
	
	def Descifrar_Clave(self,linea):
		"""
        description: decodifica el texto que recibe como parametro, sin conocer la clave de codificacion
        param texto: texto a decodificar
        return: devuelve la mejor clave para decodificar el texto
        """
		texto_descifrado=''
		linea=linea.replace('\n','')
		Clave=1
		while(not Clave==26 and linea!=''):
			if(linea.find(' ')!=-1):
				linea.replace(' ','|') #Reemplaza el espacion por |
				pos=linea.find('|') #Busca la posicion donde esta |
				palabra=linea[:pos] #Se asigna la cadena a palabra hasta la posicion
				linea.lstrip(linea[:pos+1])#Elimina hasta la posición mas uno
			else:
				palabra=linea
			for letra in palabra:
				suma=self.__abc.find(letra) - Clave
				modulo=int(suma)%len(self.__abc)
				texto_descifrado=texto_descifrado+str(self.__abc[modulo])
			man_archivo=open("words.txt") # Abre el archivo
			lineaux=man_archivo.readline() # Lee una sola linea del archivo
			while(not texto_descifrado==lineaux and lineaux!=''): # Empieza a darle sentido al 
				lineaux=man_archivo.readline()                    # texto decodificado
			lineaux=lineaux.replace('\n','') # Encuentra el salto de linea y reemplaza por un espacio
			if(lineaux!=''):
				print lineaux # Interpreto la linea del archivo
				Clave=0
			Calve=Clave+1
