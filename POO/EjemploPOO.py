#Primera Clase 
#Primera clase, modelaremos un objeto "gelatina"
"""class Gelatina: #Clase Gelatina
	
	def __init__(self, tam, color, sabor): #Creacion de el objeto$$$Self nos dara la info del objeto
		self.tam=tam        #aqui asignamos valores a los objetos q estamos creando
		self.color=color
		self.sabor=sabor
		
	def Muestra(self):      #Muestra todos los valores del objeto
		print self.tam;
		print self.color;
		print self.sabor;
		
def main():
	gel1=Gelatina("chico","rojo","fresa") #Instanciamos es decir creamos el objeto y le pasamos su caracteristicas
	gel2=Gelatina("mediana","amarilla","manzana")
	gel3=Gelatina("grande","azul","mora")
	#Lamamos al muestra
	gel1.Muestra()
	gel2.Muestra()
	gel3.Muestra()

#Comentado
#Otro Ejemplo
"""
class Televisores:
	
	def __init__(self, marca):
		self.__marca=marca
		self.encendida=False
		
	def encender(self):
		if(self.encendida==False):
			self.encendida=True
		else:
			print "La tele esta prendida"
	
	def apagar(self):
		if(self.encendida==True):
			self.encendida=False
		else:
			print "La tele esta apagada"
			
	def muestra_marca(self): #geter
		print self.__marca
		
		
def main():
	tele=Televisores("Samsung")
	tele.encender()
	tele.apagar()
	tele.apagar()
	tele.muestra_marca()
