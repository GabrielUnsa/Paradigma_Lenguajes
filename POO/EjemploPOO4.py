#Lista Enlazada en python
class Nodo:
	def __init__(self):
		self.nombre=None
		self.edad=0
		self.sig=None

class Lista:
	def __init__(self):
		self.raiz=Nodo()
	
	def insertar(self,nodo):
		if(self.raiz.nombre==None):
			self.raiz=nodo
		else:
			aux=self.raiz
			while True:				#segira el bloque hasta que pase el break
				if(aux.sig==None):
					aux.sig=nodo
					break
				else:
					aux=aux.sig
	
	def consultar(self):
		aux=self.raiz
		if(aux.nombre==None):
			print "Lista Vacia"
		else:
			print aux.nombre
			print aux.edad
			while aux.sig!=None:
				aux=aux.sig
				print aux.nombre
				print aux.edad
				
	def eliminar(self):
		aux=self.raiz
		aux2=self.raiz
		if aux.nombre==None:
			print "No hay elemento que se puedan elimiar"
		else:
			elemento=raw_input("Escriba el nombre a eliminar: ")
			if(aux.nombre==elemento):
				if(aux.sig==None):
					self.raiz=Nodo()
				else:
					self.raiz=aux.sig
			else:
				b=True
				while aux.sig!=None and b:
					aux=aux.sig
					if(aux.nombre==elemento):
						aux2.sig=aux.sig
						aux=None
						b=False
						break
					aux2=aux2.sig
				if (b==True):
					print "Nombre no encontrado"
				
				
class Principal:
	lista=Lista()
	while True:
		print "---Menu---"
		print "1.Insertar"
		print "2.Consultar"
		print "3.Eliminar"
		print "4.Salir"
		try:
			opcion=input("Elige Opcion: ")#recive un entero
			if (opcion == 1):
				nodo=Nodo()
				nodo.nombre=raw_input("Escribe tu nombre: ") #recive un nombre
				nodo.edad=input("Escribe tu Edad: ")
				lista.insertar(nodo)
			elif (opcion == 2):
				lista.consultar()
			elif (opcion == 3):
				lista.eliminar()
			elif opcion == 4:
				break
		except Exception as e:
			print "Ocurrio un error inesperado"
			print e
		

