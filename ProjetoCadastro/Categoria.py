from ProjetoCadastro.AbstractCrud import AbstractCrud

class Categoria(AbstractCrud):

	arquivo = 'db/Categorias.json'
	
	def __init__(self, nome):
		self.nome = nome

	
	
