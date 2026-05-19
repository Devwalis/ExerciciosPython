from classes.AbstractCrud import AbstractCrud

class Produto(AbstractCrud):
	def __init__(self, codigo, nome, quantidade, valor_unitario):
		self.codigo = codigo
		self.nome = nome
		self.quantidade = quantidade
		self.valor_unitario = valor_unitario
		
	


