from abc import ABC


class Imovel(ABC): 
	def __init__(self, nome, uf, valor, endereco = '', area = ''):
		self._nome= nome
		self._uf = uf
		self._valor = valor
		self._endereco = endereco
		self._area = area


	@property
	def nome(self):
		return self.nome


	@nome.setter
	def nome(self, nome):
		self._nome = nome
	

	'''
	def getNome(self):
		return self.nome
		
	def setNome(self):
		self.nome = nome
	'''

	

	
	def detalhar(self):
		print(self.__dict__)

	def calcularImposto(self)
		match self._uf:
			case 'DF': taxa = 0.03
			case 'SP': taxa = 0.04
			case 'RJ': taxa = 0.02
			case other: taxa = 0.02
			
		return self._valor * taxa


	@abstractctmethod
	def aluguelSugerido(self):
		

class ImovelResidencial(Imovel):
	def __init__(self, nome, uf, valor, endereco = '', area = ''):
		super().__init__(nome, uf, valor, endereco = '', area = '')
		self.quartos = 0
		self.piscina = false
		


class ImovelComercial(Imovel):


class ImovelRural():
	def __init__(self, hectares, curral, produtiva):
		self.hectares = ''
		self.curral = ''
		self.produtiva = True
		
	def mesPlantacao(self, mes):
		switch mes:
			case 1: print('milho')
			case 2: print('feijão')
			case 3: print('soja')
			case other: print('Algodão')

class Fazenda(ImovelRural, Imovel):


	


casa = ImovelResidencial()
casa.detalhar()



clinica = ImovelComcecial('Clinica x', 'DF', 80000)
clinica.detalhar()





'''
imovel = Imovel('Solar do cerrado', 'df', 500000)
imovel.endereco ='ABC'
imovel.area = '2000'
imovel.detalhar()


print(imovel.__dict__)

'''
