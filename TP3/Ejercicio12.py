import os
class Matriz:
				
	def __init__(self):
		self._CantFilas=0
		self.__CantColumas=0
		self.__Matriz=[]
		self.__Rala={}
	
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

	def Crea_Matriz(self):
		os.system("cls")
		x=int(raw_input("Cantidad de Filas: "))
		self.__CantFilas=x
		x=int(raw_input("Cantidad de Columnas: "))
		self.__CantColumnas=x
		for i in range(self.__CantFilas):
			self.__Matriz.append([0]*self.__CantColumnas)
		
	def Carga_Matriz(self):
		for i in range(self.__CantFilas):
			for j in range(self.__CantColumnas):
				self.__Matriz[i][j]=int(raw_input("Elemento (%d %d): "%(i+1,j+1)))

	def Matriz_Rala(self):
		#Lo comentado es para ver si una matriz es rala pero como se supone que el programa usa eso entonces no tiene sentido
		#c=0
		#cd=0
		for i in range(self.__CantFilas):
			for j in range(self.__CantColumnas):
				if(not self.__Matriz[i][j]==0):
		#			c=c+1
		#		else:
					self.__Rala[(i,j)]=[self.__Matriz[i][j]]
		#			cd=cd+1
		#if(c>cd):
		#	return True
		#else:
		#	return False	
		
	def Suma(self,Rala,Ralas):
		#Aqui estoy pasando los diccionarios a vectores para poder acceder con indices ya que en diccionario no puedo
		#Ademas que para acceder a los keys tengo q poner .keys y los valores .values
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
			#aux=c2
			#aux2=c3
			i=0
			while(i<len(b2)):
				j=0
			#	b=0
				while(j<len(c2)):
					b=0
					if(b2[i]==c2[j]):
			#			b=1
			#			k=0
						print "Posicion: "
						print b2[i]
						print "Valor: "
						print b3[i]+c3[j]
						c3[j]=0
						b=1
						
			#			while(k<=len(aux)):
			#				if(aux[k]==c2[j]):
			#					aux2[k]=m
			#					k=len(aux)
			#				k=k+1
					j=j+1
				if(b==0):
					print "Posicion: "
					print b2[i]
					print "Valor: "
					print b3[i]
					
				#if(b==0):
				#	aux=aux+b2[i]
				#	aux2=aux2+b3[i]
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
			#aux=c2
			#aux2=c3
			i=0
			while(i<len(c2)):
				j=0
			#	b=0
				while(j<len(b2)):
					b=0
					if(b2[i]==c2[j]):
			#			b=1
			#			k=0
						print "Posicion: "
						print c2[i]
						print "Valor: "
						print c3[i]+b3[j]
						b3[j]=0
						b=1
						
			#			while(k<=len(aux)):
			#				if(aux[k]==c2[j]):
			#					aux2[k]=m
			#					k=len(aux)
			#				k=k+1
					j=j+1
				if(b==0):
					print "Posicion: "
					print c2[i]
					print "Valor: "
					print c3[i]
					
				#if(b==0):
				#	aux=aux+b2[i]
				#	aux2=aux2+b3[i]
				i=i+1
	
	def Compara(self,Rala,Ralas):
		if(Rala==Ralas):
			print "Son Iguales"
		
			
		
		"""for i in range(len(c3)):
			if(b2[i]==c2[i]):
				b1=c3[i]+b3[i]
			print "Posicicion: "
			print b2[i]
			print "Valor: "
			print b1"""
			 

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
			print "-----Matriz A-----"
			matriz.Crea_Matriz()
			matriz.Carga_Matriz()
			matriz.Matriz_Rala()
			print "-----Matriz B-----"
			matriz2.Crea_Matriz()
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
	"""while(not op==0):
		if(op==1):
			print "----Matriz A------"
			x=int(raw_input("Cantidad de Filas: "))
			y=int(raw_input("Cantidad de Columnas: "))
			matriz.SetMatriz(x,y)
			matriz.Carga_Matriz()
			print "----Matriz B------"
			x=int(raw_input("Cantidad de Filas: "))
			y=int(raw_input("Cantidad de Columnas: "))
			matriz2.SetMatriz(x,y)
			matriz2.Carga_Matriz()
		elif(op==2):
			print "----Matriz A------"
			matriz.GetMatriz()
			print "----Matriz B------"
			matriz2.GetMatriz()
		elif(op==3):
			x='c'
			while((not x=='A') or (not x=='B') or (not x=='a') or (not x=='b')):
				x=raw_input("Ingrese Matriz a Mostrar: ")
			if(x=='A' or x=='a'):
				matriz.GetMatriz()
			else:
				matriz2.GetMatriz()
		elif(op==4):
			print "----Matriz A------"
			matriz.GetRala()
			print "----Matriz B------"
			matriz2.GetRala()
		elif(op==5):
			x='c'
			while((not x=='A') or (not x=='B') or (not x=='a') or (not x=='b')):
				x=raw_input("Ingrese Matriz a Mostrar: ")
			if(x=='A' or x=='a'):
				matriz.GetRala()
			else:
				matriz2.GetRala()
		elif(op==6):
			print "---Sumas De Matrices Rala-----"
			matriz.Suma(matriz.GetRala().matriz2.GetRala())
		elif(op==7):
			print "----Matriz A------"
			x=int(raw_input("Cantidad de Filas: "))
			y=int(raw_input("Cantidad de Columnas: "))
			matriz.SetMatriz(x,y)
			matriz.Carga_Matriz()
			print "----Matriz B------"
			x=int(raw_input("Cantidad de Filas: "))
			y=int(raw_input("Cantidad de Columnas: "))
			matriz2.SetMatriz(x,y)
			matriz2.Carga_Matriz()
		elif (op==8):
			x='c'
			while((not x=='A') or (not x=='B') or (not x=='a') or (not x=='b')):
				x=raw_input("Ingrese Matriz a Mostrar: ")
			if(x=='A' or x=='a'):
				x=int(raw_input("Cantidad de Filas: "))
				y=int(raw_input("Cantidad de Columnas: "))
				matriz.SetMatriz(x,y)
				matriz.Carga_Matriz()
			else:
				x=int(raw_input("Cantidad de Filas: "))
				y=int(raw_input("Cantidad de Columnas: "))
				matriz2.SetMatriz(x,y)
				matriz2.Carga_Matriz()
"""
