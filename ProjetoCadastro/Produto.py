import json

class Produto:
	def __init__(self, codigo, nome, quantidade, valor_unitario):
		self.codigo = codigo
		self.nome = nome
		self.quantidade = quantidade
		self.valor_unitario = valor_unitario
		
	

	def detalhar(self):
		return self. __dict__
	

	def inserir(self):
		try:
			with open('db/produtos.js') as file		
				lista = jso.load(file)
		except Exception:
			lista = []
			
		lista.append(self.detalhar())
		
		with open('db/produtos.json', 'w') as file:
			json.dump()
			
