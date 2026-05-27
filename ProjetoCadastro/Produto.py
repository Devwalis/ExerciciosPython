from ProjetoCadastro.AbstractCrud import AbstractCrud

class Produto(AbstractCrud):
	def __init__(self, codigo='', nome='', quantidade=0, valor_unitario=0.0):
		self.codigo = codigo
		self.nome = nome
		self.quantidade = quantidade
		self.valor_unitario = valor_unitario
		self.arquivo = "produtos.json"		
	


