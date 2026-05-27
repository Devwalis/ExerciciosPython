import json
from abc import  ABC




class AbstractCrud(ABC):


	def detalhar(self):
		return{
			"codigo": self.codigo, 
			"nome": self.nome,
			"quantidade": self.quantidade,
			"valor_unitario": self.valor_unitario
}


	#	return self.__dict__

	def inserir(self):
		
		try:
			with open(self.arquivo, 'r') as file:
				produtos = json.load(file)
		except (FileNotFoundError, json.JSONDecodeError):
			produtos = []
	
		novo_produto = {
			"codigo": self.codigo,
			"nome": self.nome,
			"quantidade": self.quantidade,
			"valor_unitario": self.valor_unitario
}
		produtos.append(novo_produto)
		
		with open(self.arquivo, 'w') as file:
			json.dump(produtos, file, indent= 4)

		print("Produto cadastrado com sucesso")

			
		
	@classmethod	
	def listarTodos(cls):
		try:
			with open("produtos.json", "r") as file:
				produtos = json.load(file)
			for i, produto in enumerate(produtos):
			
				print(f"""
	{i}

	Codigo: {produto['codigo']}
	Nome: {produto['nome']}
	Quantidade: {produto['quantidade']}
	Valor: {produto['valor_unitario']}
					""")

		except Exception as e:
			print(f"Erro ao listar produtos:{e}")



	'''	lista = cls.consultar()
		
		for i, p in enumerate(lista):
			print(f"{i} - {p}")

'''


	@classmethod
	def consultar(clf, item = None):
		try:
			with open(clf.arquivo) as file:
				lista = json.load(file)
			
			
			return lista[item] if isinstance(item, int) else lista



			#	if isinstance(item, int):
			#		return lista[item]
			#	else:
			#		return lista
		except Exception:
			return []

	
	


	def alterar(self, item):
		lista = self.consultar()
		lista[item] = self.detalhar()
		self.gravarAquivo(lista)

		print('Registro alterado com sucesso')

	def __gravarArquivo(self):
		with open(self.arquivo, 'w') as file:
			json.dump(lista, file, indent= 4)
		
		print('Operação realizada com sucesso')
	

	@classmethod
	def excluir(cls, item):
		lista = cls.consultar()

		del lista[item]

		with open(cls.arquivo, 'w') as file:
			json.dump(lista, file, indent=4)
	
		cls.__gravarArquivo(lista)

	

		
		
