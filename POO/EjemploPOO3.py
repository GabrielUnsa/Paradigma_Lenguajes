#Encapsulasion
"""class Nacimiento:
	def __init__(self):
		self.__anio=2000 #al poner '_''_' (es decir __) el atributo es privado
		self.__mes=1
		self.__dia=1
	
	def setMes(self, mes):
		if mes>0 and mes<13:
			self.__mes=mes
		else :
			print "Mes invalido"
	
	def getMes(self):
		return self.__mes

def main():
	objeto = Nacimiento()
	objeto.setMes(45)
	print objeto.getMes()
	objeto.setMes(6)
	print objeto.getMes()
	objeto.setMes(12)
	print objeto.getMes()"""
#Otro ejemplo de encapsulacion
#Python ya tiene polimorfismo
class Television:
	
	def __init__(self, marca):
		self.__marca=marca
		self.encendida=False
		
	def encenderT(self):
		if(self.encendida==False):
			self.encendida=True
		else:
			print "La television ya estaba encendida"
		
	def apagarT(self):
		if(self.encendida==True):
			self.encendida=False
		else:
			print "La television ya estaba apagada"
	
	def getMarca(self):
		return self.__marca

def main():		
	tele = Television("Samsung")
	tele.encenderT()
	tele.apagarT()
	print tele.getMarca()

