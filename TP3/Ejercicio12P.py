import os
class Matriz:
				
	def __init__(self):						"""Instancia donde creamos el objeto Matriz"""
		self._CantFilas=0
		self.__CantColumas=0
		self.__Matriz=[]
		self.__Rala={}
		
	#Seter's y Geter's de los atributos
	def SetColumna(self,columna):				
		self.__CantColumnas=columna
	
	def SetFila(self,fila):
		self.__CantFilas=filas
	
	def GetRala(self):
		return self.__Rala
	
	def GetFilas(self):
		return self.__CantFilas

	def GetColumnas(self):
		return self.__CantColumnas
	
	def GetMatriz(self):
		return self.__Matriz
	#Funciones
	def Crea_Matriz(self):								"""Crea una Matriz"""
		os.system("cls")
		x=int(raw_input("Cantidad de Filas: "))
		self.__CantFilas=x
		x=int(raw_input("Cantidad de Columnas: "))
		self.__CantColumnas=x
		self.__Matriz=[]
		for i in range(self.__CantFilas):
			self.__Matriz.append([0]*self.__CantColumnas)
		
	def Carga_Matriz(self):									"""Carga Una Matriz"""
		for i in range(self.__CantFilas):
			for j in range(self.__CantColumnas):
				self.__Matriz[i][j]=int(raw_input("Elemento (%d %d): "%(i+1,j+1)))
	
	
	def Matriz_Rala(self):									"""Crea Mattriz Hueca o Rala"""
		for i in range(self.__CantFilas):
			for j in range(self.__CantColumnas):
				if(not self.__Matriz[i][j]==0):
					self.__Rala[(i,j)]=[self.__Matriz[i][j]]
		
	def Suma(self,Rala,Ralas):								"""Suma Las Matrices Rala"""
		b1=Rala.values()
		b2=Rala.keys()
		c1=Ralas.values()
		c2=Ralas.keys()
		b3=[]
		c3=[]
		for i in range(len(b1)):
			b3=b3+b1[i]
		for i in range(len(c1)):
			c3=c3+c1[i]
		if(len(c3)<len(b3)):
			i=0
			while(i<len(b2)):
				j=0
				while(j<len(c2)):
					b=0
					if(b2[i]==c2[j]):
						print "Posicion: "
						print b2[i]
						print "Valor: "
						print b3[i]+c3[j]
						c3[j]=0
						b=1
					j=j+1
				if(b==0):
					print "Posicion: "
					print b2[i]
					print "Valor: "
					print b3[i]
				i=i+1	
		elif(len(c3)==len(b3)):
			for i in range(len(c3)):
				if(b2[i]==c2[i]):
					b1=c3[i]+b3[i]
				print "Posicicion: "
				print b2[i]
				print "Valor: "
				print b1
		else:
			i=0
			while(i<len(c2)):
				j=0
				while(j<len(b2)):
					b=0
					if(b2[i]==c2[j]):
						print "Posicion: "
						print c2[i]
						print "Valor: "
						print c3[i]+b3[j]
						b3[j]=0
						b=1
					j=j+1
				if(b==0):
					print "Posicion: "
					print c2[i]
					print "Valor: "
					print c3[i]
				i=i+1
	
	def Compara(self,Rala,Ralas):
		if(Rala==Ralas):
			print "Son Iguales"
def menu():
	op=10
	os.system("cls")
	while(op<0 or op>7):
		print "1. Cargar Matrices"
		print "2. Mostrar Matrices"
		print "3. Mostrar una Matriz"
		print "4. Mostrar Matrices Rala"
		print "5. Muestra una Matriz Rala"
		print "6. Sumar Matrices"
		print "7. Comparar Matrices"
		print "0. Salir"
		op=int(raw_input("opcion: "))
	return op
		
		
def main():
#Programa funciona con dos matrices
	matriz=Matriz()
	matriz2=Matriz()
	op=menu()
	while(not op==0):
		os.system("cls")
		if(op==1):
			matriz.Crea_Matriz()
			print "-----Matriz A-----"
			matriz.Carga_Matriz()
			matriz.Matriz_Rala()
			matriz2.Crea_Matriz()
			print "-----Matriz B-----"
			matriz2.Carga_Matriz()
			matriz2.Matriz_Rala()
		elif(op==2):
			print "----Matriz A------"
			print matriz.GetMatriz()
			print "----Matriz B------"
			print matriz2.GetMatriz()
		elif(op==3):
			x='c'
			while((not x=='A') and (not x=='B') and (not x=='a') and (not x=='b')):
				x=raw_input("Ingrese Matriz a Mostrar: ")
			if(x=='A' or x=='a'):
				print matriz.GetMatriz()
			else:
				print matriz2.GetMatriz()
		elif(op==4):
			print "----Matriz A------"
			print matriz.GetRala()
			print "----Matriz B------"
			print matriz2.GetRala()
		elif(op==5):
			x='c'
			while((not x=='A') and (not x=='B') and (not x=='a') and (not x=='b')):
				x=raw_input("Ingrese Matriz a Mostrar: ")
			if(x=='A' or x=='a'):
				print matriz.GetRala()
			else:
				print matriz2.GetRala()
		elif(op==6):
			if(matriz.GetFilas()==matriz2.GetFilas() and matriz.GetColumnas()==matriz2.GetColumnas()):
				matriz.Suma(matriz.GetRala(),matriz2.GetRala())
			else:
				print "No se Pueden Sumar Matrices}"	
		elif(op==7):
			if(len(matriz.GetRala())==len(matriz2.GetRala())):
				matriz.Compara(matriz.GetRala(),matriz2.GetRala())
			else:
				print "Las matrices ralas no poseen el mismo tamano" 
		x=raw_input("Precione Enter para continuar......")
		op=menu()
main()
