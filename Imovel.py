class Imovel:
	def __init__(self, nome, uf, valor, endereco = '', area = ''):
		self.nome= nome
		self.uf = uf
		self.valor = valor
		self.endereco = endereco
		self.area = area
	
	def detalhar(self):
		print(self.__dict__)
		

	
		

	def calcularImposto(self)
		return self.valor * 0.02

class ImovelResidencial(Imovel):



class ImovelComercial(Imovel):


casa = ImovelResidencial()
print(casa)






imovel = Imovel('Solar do cerrado', 'df', 500000)
imovel.endereco ='ABC'
imovel.area = '2000'
imovel.detalhar()


print(imovel.__dict__)

