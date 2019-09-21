#Herencia
class Electrodomestico:
	
	def __init__(self,nombre):
		self.nombre=nombre
		self.estado=False
		
	def encederE(self):  
		if(self.estado==False):
			self.estado=True
			print "Se ha encendido: "+self.nombre
		else:
			print "El elestrodomestico esta ensendido"
			
	def apagar(self):
		if (self.estado==True):
			self.estado=False
			print "Se ha apagado: "+self.nombre
		else:
			print "El electrodomestico esta apagado"
	
class Telefono:
	def llamar(self):
		print "Llamando....."
	def colgar(self):
		print "Llamada Finalizada"
"""class Celular(Electrodomestico):
	
	def mandarMensaje(self):
		if (self.estado==True):
			print "Mandando Mensaje"
"""	

class Celular(Electrodomestico,Telefono):
	
	def mandarMensaje(self):
		if (self.estado==True):
			print "Mandando Mensaje"
			
			
class Televisor(Electrodomestico):
	def cambiarCanal(self):
		if(self.estado==True):
			print "Cambiando de canal"

def main():
	cel=Celular("Celu")
	cel.encederE()
	cel.mandarMensaje()
	cel.llamar()
	cel.colgar()
	cel.apagar()
	tel=Televisor("Tele")
	tel.encederE()
	tel.cambiarCanal()
	tel.apagar()
	
