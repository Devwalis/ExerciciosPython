import json
from abc import  ABC




class AbstractCrud(ABC):


	def detalhar(self):
		return self.__dict__

	def inserir(self):


		lista = self.consultar()
		
		lista.append(self.detalhar())
		
		self.gravarArquivo(lista)

		print('Registro cadastrado com sucesso')
		
	@classmethod	
	def listarTodos(cls):
		lista = cls.consultar()
		
		for i, p in enumerate(lista):
			print(f"{i} - {p}")

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

	

		
		
