class CasaStark:
	"""Un raro ejemplo"""
	print("Hijos de Eddard Stark y Lady Catelyn")
	def __init__(self,apellido_stark):
		self.apellido_stark=apellido_stark
	
class HerederoStar(CasaStark):
	"""Sub-Clase"""
	def nombre(self,nombre,apellido_stark):
		print("Mi nombre es: ",nombre," Heredero de la casa: ",apellido_stark)
	
#Instancia Objeto Heredero
def main():
	robb=HerederoStar("Stark")
	sansa=HerederoStar("Stark")
	arya=HerederoStar("Stark")
	bran=HerederoStar("Stark")
	rickon=HerederoStar("Stark")
#Accedemos a Metodos
	print(robb.nombre("Robb ",robb.apellido_stark))
	print(sansa.nombre("Sansa ",sansa.apellido_stark))
	print(arya.nombre("Arya ",arya.apellido_stark))
	print(bran.nombre("Bran ",bran.apellido_stark))
	print(rickon.nombre("Rickon ",rickon.apellido_stark))
